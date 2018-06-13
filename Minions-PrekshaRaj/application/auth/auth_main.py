"""
This module is for all superuser level auth use
highly sensitive
please use caution

3/5/2016

by Chengxi (Chen) Shi

"""


class DynamoAuth(object):
    """
    This is the one for DynamoDB on AWS
    """

    region = "us-west-2"
    access_key = "prek"
    secret_key = "prek"
    """
    # Shitai's personal: please do not copy the ones below
    access_key = "AKIAJSGEZ3CZ2EZWIXQQ"
    secret_key = "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"
    """
    # Chen's personal: please do not copy the ones below
    #access_key = "AKIAIZ4HUJSPT27D3UXQ"
    #secret_key = "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"
    # the auth keys below is the one from Joey for Taichi's use
    # access_key = "AKIAIUX4VUX3LOZF3IYA"
    # secret_key = "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"


application_secret_key = 'EpwoqEwqsapoqweqw23w'

"""
Credentials for accessing plaid server
"""
plaid_client_id = '56d755d5152e16ec4a511ed2'
plaid_secret = 'aeac07d4a9e788ee0ba8927f581f80'
plaid_public_key = 'e0b76efbe31c0b5b84c7bd47688478'
