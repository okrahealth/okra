""" Batch job utilities. """

from okra.exceptions import UrlJoinError



def check_urljoin(cache: str, fname: str, fpath: str) -> bool:
    if fpath == fname:

        exp = 'cache: {}, fname: {}, fpath: {}'.\
            format(cache, fname, fpath)
        raise UrlJoinError(expression=exp, message='incorrect urljoin')

    return True
