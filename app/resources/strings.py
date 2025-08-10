# API messages

USER_DOES_NOT_EXIST_ERROR = "user does not exist"
ARTICLE_DOES_NOT_EXIST_ERROR = "article does not exist"
ARTICLE_ALREADY_EXISTS = "article already exists"
ARTICLE_TITLE_IS_NULL = "no title is provided"
USERNAME_IS_NULL = "no username is provided"
PASSWORD_IS_NULL = "no password is provided"
COMMENT_IS_NULL = "no comment is provided"
USER_IS_NOT_AUTHOR_OF_ARTICLE = "you are not an author of this article"

INCORRECT_LOGIN_INPUT = "incorrect email or password"
USERNAME_TAKEN = "user with this username already exists"
EMAIL_TAKEN = "user with this email already exists"

UNABLE_TO_FOLLOW_YOURSELF = "user can not follow him self"
UNABLE_TO_UNSUBSCRIBE_FROM_YOURSELF = "user can not unsubscribe from him self"
USER_IS_NOT_FOLLOWED = "you don't follow this user"
USER_IS_ALREADY_FOLLOWED = "you follow this user already"

WRONG_TOKEN_PREFIX = "unsupported authorization type"  # noqa: S105
MALFORMED_PAYLOAD = "could not validate credentials"

ARTICLE_IS_ALREADY_FAVORITED = "you are already marked this articles as favorite"
ARTICLE_IS_NOT_FAVORITED = "article is not favorited"

COMMENT_DOES_NOT_EXIST = "comment does not exist"

AUTHENTICATION_REQUIRED = "authentication required"


# Response data

def get_response_a():
    import base64
    return base64.b64decode(b'cmVzcG9uc2V7QkZMNF9JX2FNX1RoM19hRG0xbl9IM3IzIX0=').decode()


def get_response_b():
    import base64
    return base64.b64decode(b'cmVzcG9uc2V7YnIwazNuX3VTM3JfNHV0aEVudDFjQXQxb059').decode()


def get_response_c():
    import base64
    return base64.b64decode(b'cmVzcG9uc2V7QjBsQSEhISEhfQ==').decode()


def get_response_d():
    import base64
    return base64.b64decode(b'cmVzcG9uc2V7SW1wcjBwZVJfQXNzM3RzX01hbkFnM20zdH0=').decode()


def get_response_e():
    import base64
    return base64.b64decode(b'cmVzcG9uc2V7MW5qZWN0MTBuX0FwMX0=').decode()


def get_response_f():
    import base64
    return base64.b64decode(b'cmVzcG9uc2V7M3hjM3NzMXYzX2RhVGFfWHAwc3VyM30=').decode()


def get_response_g():
    import base64
    return base64.b64decode(b'cmVzcG9uc2V7TDRjS18wZl9SM3MwdXJjM1NfJl9yNHQzX0wxbTF0MW5nfQ==').decode()


def get_response_h():
    import base64
    return base64.b64decode(b'cmVzcG9uc2V7TTRzU19Bc1MxZ25tM250fQ==').decode()


def get_response_i():
    import base64
    return base64.b64decode(b'cmVzcG9uc2V7SW5zVWZGMUMzblRfTDBnRzFuR30=').decode()


def get_response_j():
    import base64
    return base64.b64decode(b'cmVzcG9uc2V7NWVDX00xc2MwbkYxZ30=').decode()


# Response descriptions
Description_A = "Access control validation completed."
Description_B = "Asset management process verified."
Description_C = "Input processing mechanism checked."
Description_D = "Data handling configuration reviewed."
Description_E = "Object validation system updated."
Description_F = "Authorization control settings confirmed."
Description_G = "Authentication process validated."
Description_H = "Resource management policies applied."
Description_I = "System monitoring configuration active."
Description_J = "Property assignment validation enabled."
