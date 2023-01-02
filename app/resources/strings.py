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


# Flags

def BrokenFunctionLevelAuthorization():
    return "flag{BFL4_I_aM_Th3_aDm1n_H3r3!}"


def BrokenUserAuthentication():
    return "flag{br0k3n_uS3r_4uthEnt1cAt1oN}"


def BOLA():
    return "flag{B0lA!!!!!}"


def ImproperAssetsManagement():
    return "flag{Impr0peR_Ass3ts_ManAg3m3nt}"


def Injection():
    return "flag{1nject10n_Ap1}"


def ExcessiveDataExposure():
    return "flag{3xc3ss1v3_daTa_Xp0sur3}"


def LackOf():
    return "flag{L4cK_0f_R3s0urc3S_&_r4t3_L1m1t1ng}"


def MassAssignment():
    return "flag{M4sS_AsS1gnm3nt}"


def InsufficientLogging():
    return "flag{InsUfF1C3nT_L0gG1nG}"


def SecMiss():  # not in used in app (external flag)
    return "flag{5eC_M1sc0nF1g}"


# Description
DescriptionInsufficientLogging = "Insufficient logging and monitoring, coupled with missing or ineffective " \
                                 "integration with incident response, " \
                                 "allows attackers to further attack systems, maintain persistence, pivot to more " \
                                 "systems to tamper with, extract, or destroy data. " \
                                 "Most breach studies demonstrate the time to detect a breach is over 200 days, " \
                                 "typically detected by external parties rather than internal processes or monitoring."
DescriptionImproperAssetsManagement = "Old API versions are usually unpatched and are an easy way to compromise " \
                                      "systems without having to fight " \
                                      "state-of-the-art security mechanisms, which might be in place to protect the " \
                                      "most recent API versions. "
DescriptionInjection = "Attackers will feed the API with " \
                       "malicious data through whatever " \
                       "injection vectors are available " \
                       "(e.g., direct input, parameters, " \
                       "integrated services, etc.), " \
                       "expecting it to be sent to an " \
                       "interpreter"
DescriptionExcessiveDataExposure = "Exploitation of Excessive Data " \
                                   "Exposure is simple, and is usually " \
                                   "performed by sniffing the traffic " \
                                   "to analyze the API responses, " \
                                   "looking for sensitive data " \
                                   "exposure that should not be " \
                                   "returned to the user."
DescriptionBOLA = "APIs tend to expose endpoints that handle object identifiers, " \
                  "creating a wide attack surface Level Access Control issue. Object " \
                  "level authorization checks should be considered in every function " \
                  "that accesses a data source using an input from the user."
DescriptionBrokenFunctionLevelAuthorization = "Complex access control policies with different hierarchies, " \
                                              "groups, and roles, and an unclear separation between " \
                                              "administrative and regular functions, tend to lead to authorization " \
                                              "flaws. By exploiting these issues, attackers gain access to other " \
                                              "users’ resources and/or administrative functions."
DescriptionBrokenUserAuthentication = "Authentication mechanisms are often implemented incorrectly, " \
                                      "allowing attackers to compromise authentication tokens or to " \
                                      "exploit implementation flaws to assume other user's identities " \
                                      "temporarily or permanently. Compromising system's ability to " \
                                      "identify the client/user, compromises API security overall."
DescriptionLackOf = "Quite often, APIs do not impose any restrictions on the size or " \
                    "number of resources that can be requested by the client/user. Not " \
                    "only can this impact the API server performance, leading to " \
                    "Denial of Service (DoS), but also leaves the door open to " \
                    "authentication flaws such as brute force."
DescriptionMassAssignment = "Binding client provided data (e.g., JSON) to data models, without " \
                            "proper properties filtering based on a whitelist, usually lead to " \
                            "Mass Assignment. Either guessing objects properties, exploring " \
                            "other API endpoints, reading the documentation, or providing " \
                            "additional object properties in request payloads, allows attackers " \
                            "to modify object properties they are not supposed to."
