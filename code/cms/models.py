from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator
from django.core.exceptions import ValidationError

def check_age(value):
    if value < 0 or value > 150:
        raise ValidationError('有効範囲は0歳から150歳です')


class Member(models.Model):

    #  性別を選択する選択肢を宣言
    GENDER_CHOICES = (
        (1, '男性'),
        (2, '女性'),
        (3, 'その他'),
    )

    # フィールドを定義します
    # verbose_name：人間に表示する名前を決める、adminサイトとかで使う
    name = models.CharField(max_length=255, verbose_name='名前', blank=True, null=True)  # max_lengthは長さの最大値
    # choicesにタプルを指定することで選択肢のエリアにできる、
    # blankやnullをOKにするかどうか

    name_read = models.CharField(max_length=255, verbose_name='フリガナ', blank=True, null=True)  # max_lengthは長さの最大値
    age = models.IntegerField(default=0, validators=[check_age])
    gender = models.IntegerField(verbose_name='性別', choices=GENDER_CHOICES, blank=True, null=True)
    birth_day = models.DateField(verbose_name='誕生日', blank=True, null=True)
    email = models.EmailField(verbose_name='メールアドレス', max_length=256, blank=True, null=True)
    telephone = models.CharField(verbose_name='電話番号', max_length=100, blank=True, null=True)
    zip_code = models.CharField(verbose_name='郵便番号', max_length=20, blank=True, null=True)
    prefectures = models.CharField(verbose_name='都道府県', max_length=20, blank=True, null=True)
    address_line1 = models.CharField(verbose_name='住所1', max_length=100, blank=True, null=True)
    address_line2 = models.CharField(verbose_name='住所2', max_length=100, blank=True, null=True)
    house = models.CharField(verbose_name='建物名', max_length=100, blank=True, null=True)
    remark = models.CharField(verbose_name='備考', max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成時間', auto_now_add=True)  # レコードが追加された時にその時間を保存します
    updated_at = models.DateTimeField(verbose_name='更新時間', auto_now=True)  # レコードが更新されたタイミングで現在時間が保存されます。
    visit_num = models.IntegerField(verbose_name='来店回数', blank=True, null=True, default=0)
    latest_visit_day = models.DateField(verbose_name=' 直近の来店日', blank=True, null=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    order_day = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.member.name + ":" + str(self.order_day)

class Drink(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    drink_name = models.CharField(verbose_name='ドリンク名', max_length=100, blank=True, null=True)
    drink_num = models.IntegerField(verbose_name='ドリンク個数', default=1, blank=True, null=True)

    def __str__(self):
        return str(self.pk) + ":" + self.drink_name

class Course(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    course_name = models.CharField(verbose_name='コース名', max_length=100, blank=True, null=True)
    course_num = models.IntegerField(verbose_name='コース個数', default=1, blank=True, null=True)

# カテゴリマスタ
class MenuCategory(models.Model):
    category_name = models.CharField('カテゴリ', max_length=255)

    def __str__(self):
        return self.category_name

class Goods(models.Model):
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)
    goods_name = models.CharField('商品', max_length=255)

    def __str__(self):
        return self.goods_name

