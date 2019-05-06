""" Populate SQL database. 

References:
  https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
"""
import logging
from urllib.parse import urljoin

from okra.models import DataAccessLayer, Inventory, Meta
from okra.github import repo_to_objects
from okra.gitlogs import parse_inventory

logger = logging.getLogger(__name__)


def insert_buffer(items: iter, dal, buffer_size=1024):
    """ Insert items using a buffer. 

    :param items: sqlalchemy orm database objects
    :param dal: okra.models.DataAccessLayer
    :param invobj: okra.models.Inventory object, to be updated
    :buffer_size: number of items to add before committing a session
    """
    logger.info("STARTED insert buffer")
    count = 0
    for item in items:
        
        dal.session.add(item)

        if count % buffer_size == 0:
            try:
                dal.session.commit()
                logger.info("Committed db objects: {}".format(count))
                
            except Exception as exc:
                dal.session.rollback()
                logger.error("Rolled back session")
                logger.exception(exc)
                raise exc

        count += 1

    try:
        dal.session.commit()
        logger.info("Committed db objects: {}".format(count))

    except Exception as exc:
        dal.session.rollback()
        logger.error("Rolled back session")
        logger.exception(exc)
        raise exc

    logger.info("COMPLETED insert buffer")

def populate_db(dburl: str, cache: str, repo_name: str, buffer_size=1024):
    """ Populate a new or existing database. """

    logger.info("STARTED populating db: {}".format(dburl))
    
    # Initialize data access layer
    
    dal = DataAccessLayer(dburl)
    dal.connect()
    dal.session = dal.Session()

    owner, project = repo_name.split("/")
    rpath = urljoin(cache, repo_name)

    # Check or get git repo inventory information

    last_commit = ""
    invobj = dal.session.query(
        Inventory.project_name, Inventory.owner_name,
        Inventory.last_commit).\
        filter(Inventory.project_name == project,
               Inventory.owner_name == owner).first() # unique value

    if invobj is not None:
        last_commit = invobj.last_commit

    # insert relevant commits into database
        
    objs = repo_to_objects(repo_name, cache, last_commit)
    insert_buffer(objs, dal, buffer_size)

    # update inventory

    invmsg = parse_inventory(rpath, repo_name)

    if len(last_commit) > 0:

        # Retrieve new object b/c old object is no longer in session
            
        inv = dal.session.query(
            Inventory.project_name, Inventory.owner_name,
            Inventory.last_commit).\
            filter(Inventory.project_name == project,
                   Inventory.owner_name == owner).first() # unique value

        # Do not try updating database if object hasn't changed
            
        if inv.last_commit != invmsg.last_hash:
            inv.last_commit = invmsg.last_hash
            dal.session.add(inv)
            dal.session.commit()
    
    else:

        # Add new inventory object
            
        inv = Inventory(
            owner_name = invmsg.owner,
            project_name = invmsg.project,
            last_commit = invmsg.last_hash)

        dal.session.add(inv)
        dal.session.commit()

    dal.session.close()
    logger.info("FINISHED populating db: {}".format(dburl))

    
