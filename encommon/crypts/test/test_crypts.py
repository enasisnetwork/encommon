"""
Functions and routines associated with Enasis Network Common Library.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from pytest import fixture
from pytest import mark
from pytest import raises

from ..crypts import Crypts



@fixture
def phrases() -> dict[str, str]:
    """
    Construct randomly generated Fernet keys for passphrases.

    :returns: Randomly generated Fernet keys for passphrases.
    """

    return {
        'default': Crypts.keygen(),
        'secrets': Crypts.keygen()}



def test_Crypts(
    phrases: dict[str, str],
) -> None:
    """
    Perform various tests associated with relevant routines.

    :param phrases: Dictionary of randomly generated phrases.
    """

    crypts = Crypts(phrases)


    attrs = list(crypts.__dict__)

    assert attrs == [
        '_Crypts__phrases']


    assert repr(crypts)[:23] == (
        '<encommon.crypts.crypts')

    assert hash(crypts) > 0

    assert str(crypts)[:23] == (
        '<encommon.crypts.crypts')


    assert crypts.phrases == phrases
    assert len(crypts.keygen()) == 44



@mark.parametrize(
    'value,unique',
    [('foo', 'default'),
     ('foo', 'secrets')])
def test_Crypts_iterate(
    value: str,
    unique: str,
    phrases: dict[str, str],
) -> None:
    """
    Perform various tests associated with relevant routines.

    :param value: String value that will returned encrypted.
    :param unique: Unique identifier of mapping passphrase.
    :param phrases: Dictionary of randomly generated phrases.
    """

    crypts = Crypts(phrases)

    encrypt = crypts.encrypt(value, unique)

    split = encrypt.split(';')

    assert split[1] == '1.0'
    assert split[2] == unique

    decrypt = crypts.decrypt(encrypt)

    assert decrypt == value



def test_Crypts_raises(
    phrases: dict[str, str],
) -> None:
    """
    Perform various tests associated with relevant routines.

    :param phrases: Dictionary of randomly generated phrases.
    """


    with raises(ValueError) as reason:
        Crypts({'foo': 'bar'})

    assert str(reason.value) == 'default'


    crypts = Crypts(phrases)


    with raises(ValueError) as reason:
        crypts.decrypt('foo')

    assert str(reason.value) == 'string'


    with raises(ValueError) as reason:
        string = '$ENCRYPT;1.1;f;oo'
        crypts.decrypt(string)

    assert str(reason.value) == 'version'
