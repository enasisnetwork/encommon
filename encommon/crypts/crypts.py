"""
Functions and routines associated with Enasis Network Common Library.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from re import compile
from re import match as re_match
from re import sub as re_sub

from cryptography.fernet import Fernet



ENCRYPT = compile(
    r'^\$ENCRYPT;1\.\d;\S+\;.+?$')



class Crypts:
    """
    Encrypt and decrypt values using passphrase dictionary.

    Example
    -------
    >>> phrase = Crypts.keygen()
    >>> crypts = Crypts({'default': phrase})
    >>> encrypt = crypts.encrypt('example')
    >>> crypts.decrypt(encrypt)
    'example'

    :param phrases: Passphrases that are used in operations.
    """

    __phrases: dict[str, str]


    def __init__(
        self,
        phrases: dict[str, str],
    ) -> None:
        """
        Initialize instance for class using provided parameters.
        """

        if 'default' not in phrases:
            raise ValueError('default')

        self.__phrases = dict(phrases)


    @property
    def phrases(
        self,
    ) -> dict[str, str]:
        """
        Return the property for attribute from the class instance.

        :returns: Property for attribute from the class instance.
        """

        return dict(self.__phrases)


    def encrypt(
        self,
        value: str,
        unique: str = 'default',
    ) -> str:
        """
        Encrypt the provided value with the relevant passphrase.

        :param value: String value that will returned encrypted.
        :param unique: Unique identifier of mapping passphrase.
        :returns: Encrypted value using the relevant passphrase.
        """

        phrase = self.__phrases[unique]

        encrypt = (
            Fernet(phrase)
            .encrypt(value.encode())
            .decode())

        return (
            '$ENCRYPT;1.0;'
            f'{unique};{encrypt}')


    def decrypt(
        self,
        value: str,
    ) -> str:
        """
        Decrypt the provided value with the relevant passphrase.

        :param value: String value that will returned decrypted.
        :returns: Decrypted value using the relevant passphrase.
        """

        value = crypt_clean(value)

        if not re_match(ENCRYPT, value):
            raise ValueError('string')

        version, unique, value = (
            value.split(';')[1:])

        if version != '1.0':
            raise ValueError('version')

        phrase = self.__phrases[unique]

        return (
            Fernet(phrase)
            .decrypt(value.encode())
            .decode())


    @classmethod
    def keygen(
        cls: object,
    ) -> str:
        """
        Return new randomly generated Fernet key for passphrase.

        :returns: Randomly generated Fernet key for passphrase.
        """

        key = Fernet.generate_key()

        return key.decode()



def crypt_clean(
    value: str,
) -> str:
    """
    Return the parsed and normalized encrypted string value.

    :param value: String value that will returned decrypted.
    """

    return re_sub(r'[\n\s]', '', value)
