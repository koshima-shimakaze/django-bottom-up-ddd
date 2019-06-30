import dataclasses


@dataclasses.dataclass(frozen=True)
class UserId:
    id: int


@dataclasses.dataclass(frozen=True)
class UserName:
    name: str


class User:
    def __init__(self, user_id: UserId, user_name: UserName):
        """
        Userクラス.

        Args:
            user_id (UserId): ユーザーID型
            user_name (UserName): ユーザーネーム型
        """
        self.user_id = user_id
        self.user_name = user_name


@dataclasses.dataclass(frozen=True)
class FullName:
    family_name: str
    first_name: str

    NAME_LENGTH = 50

    def __post_init__(self):
        """
        インスタンス生成時にコンストラクタに埋め込む時のもの

        インスタンス生成時にコンストラクタに埋め込むもの

        Raises:
            Exception: 文字数のException
            ValueError: NULLかどうかのException
        """
        if (self.family_name is None) or (self.first_name is None):
            error_message = "NULLを入力しないでください"
            raise ValueError(error_message)

        if (len(self.family_name) > self.NAME_LENGTH) or (
            len(self.first_name) > self.NAME_LENGTH
        ):
            error_message = "50文字以下にしてください"
            raise Exception(error_message)

    def __eq__(self, other: object) -> bool:
        """
        オブジェクト同士の比較を行う.

        オブジェクト同士の比較を行って結果を返す.

        Args:
            other (object): FullName型のオブジェクト.

        Returns:
            bool: オブジェクト同士の比較を行なった際のTrueかFalseの結果
        """
        eq_first_name = self.first_name is other.first_name
        eq_family_name = self.family_name is other.family_name
        return eq_first_name and eq_family_name and isinstance(other, FullName)


if __name__ == "__main__":
    full_name = FullName("matsuoka", "kota")
    print(full_name.family_name, full_name.first_name)

    full_name = FullName("tanaka", "hiroshi")
    print(full_name.family_name, full_name.first_name)

    # 同一の値オブジェクト同士を同じオブジェクトと判断できる
    full_name1 = FullName("matsuoka", "kota")
    full_name2 = FullName("tanaka", "hiroshi")
    print(full_name1 == full_name1)
    print(full_name1 == full_name2)

    # 間違った代入はさせない 整数型
    full_name = FullName("matsuoka", 10)
    print(full_name)

    # 間違った代入はさせない NULL
    full_name = FullName("matsuoka", None)
    print(full_name)

    # UserId と UserName
    user_id = UserId(1)
    user_name = UserName("kota")

    # 正しい代入
    # 間違った代入
    user_valid = User(user_id, user_name)
    user_invalid = User(user_name, user_id)

    print("user_valid : ", user_valid)
    print("user_invalid : ", user_invalid)
