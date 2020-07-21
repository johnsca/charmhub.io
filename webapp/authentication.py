def is_canonical_employee_authenticated(session):
    """
    Checks if the user is authenticated from SSO
    and it is a Canonical employee
    """
    return "openid" in session


def is_authenticated(session):
    """
    Checks if the user is authenticated from the session
    Returns True if the user is authenticated
    """
    return "publisher-auth" in session


def empty_session(session):
    """
    Empty the session, used to logout.
    """
    session.pop("openid", None)
    session.pop("publisher", None)
    session.pop("publisher-auth", None)
    session.pop("publisher-macaroon", None)
