""" メソッドルール
通常/クラス/スタティックがある
 - 通常メソッドは普通のインスタンスメソッド：第一引数に利用インタンスが指定可能
 - クラスメソッドのクラスのメンバ変数が利用可能（Ruby等のクラスメソッド）
 - スタティックメソッドのクラスのメンバ変数が利用不可（Javaのスタティックメソッド）

private, protectedな概念はない
->prefixとしてアンダースコアを2つつけること(__)でprivateっぽい動きになる
"""
class C(object):
    # クラス変数
    # ->クラス名.変数名でアクセス(C.val)
    val = 20

    def __init__(self):
        # インスタンス変数
        # ->インスタンス名.変数名でアクセス(i=C(); i.val)
        # ->クラス内はself.変数名でアクセス(i=C(); i.val)
        self.val = 1
        # privateっぽい変数
        self.__pval = 4
        """ 外からアクセスする場合は以下のようにする
        i = C()
        i.C__pval
        """

    def normal_method(self, v):
        """ 通常メソッド
        i = C()
        i.normal_method(5)    # i.val + 5 = 1 + 5 = 8
        C.normal_method(i, 6) # i.val + 6 = 1 + 6 = 9
        C.normal_method(C, 7) # C.val + 7 = 20 + 7 = 29
        C.normal_method(5)    # requires 2 args but 1: error
        """
        return self.val

    @classmethod
    def class_method(cls, v):
        """ クラスメソッド
        i.class_method(6) # C.val + 6 = 20 + 6 = 29
        C.class_method(8) # C.val + 8 = 20 + 8 = 31
        """
        return cls.val + v

    @staticmethod
    def static_method(v):
        """ クラスメソッド
        i.static_method(7) # C.val + 7 = 20 + 7 = 31
        C.static_method(9) # C.val + 9 = 20 + 9 = 33
        """
        return C.val + v
