# API messages
import base64

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


### Flags

def BrokenFunctionLevelAuthorization():
    return base64.b16decode("666C61677B42464C345F495F614D5F5468335F61446D316E5F48337233217D").decode("utf-8")


def BrokenUserAuthentication():
    return base64.b16decode("666C61677B6272306B336E5F755333725F34757468456E7431634174316F4E7D").decode("utf-8")


def BOLA():
    return base64.b16decode("666C61677B42306C4121212121217D").decode("utf-8")


def ImproperAssetsManagement():
    return base64.b16decode("666C61677B496D7072307065525F4173733374735F4D616E4167336D336E747D").decode("utf-8")


def Injection():
    return base64.b16decode("666C61677B316E6A65637431306E5F4170317D").decode("utf-8")


def ExcessiveDataExposure():
    return base64.b16decode("666C61677B3378633373733176335F646154615F587030737572337D").decode("utf-8")


def LackOf():
    return base64.b16decode("666C61677B4C34634B5F30665F5233733075726333535F265F723474335F4C316D3174316E677D").decode(
        "utf-8")


def MassAssignment():
    return base64.b16decode("666C61677B4D3473535F41735331676E6D336E747D").decode("utf-8")


def InsufficientLogging():
    return base64.b16decode("666C61677B496E735566463143336E545F4C306747316E477D").decode("utf-8")


def SecMiss():  # not in used embeded
    return base64.b16decode("666C61677B3565435F4D317363306E4631677D").decode("utf-8")


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
