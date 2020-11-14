$(function () {
    $('#visit_date').datepicker({
        format: 'yyyy-mm-dd',
        language: 'ja'
    });
})

$(function () {
    $('#add').on('click', function () {
        // 選択されたカテゴリ取得
        var strCategory = $('[name=category] option:selected').text();
        // 商品
        var strGoods = $('[name=goods] option:selected').text();
        // 個数
        var strNum = $('[name=num] option:selected').text();
        // formがhiddenの時
        // if ($('#order_').css('display') == 'none') {
        //     // 初期表示の時
        //     // order_0を表示する
        //     $('#order_').show();
        //     // 各idに0を追加する

        // } else {
        //     // order_0がhiddenではない場合
        //     // <div id='order_0'>をコピーする
        //     $('#order_').clone().appendTo('#content_regist');
        //     // 各idを書き換える

        // }

        // <div id='order_'>をコピーする
        // var order = $('#order_').clone(true).find('#tdCategory_, #tdGoods_, #tdNum_, #btnEdit_, #btnDel_').each(function () {
        //     console.log($(this).attr('id'));
        //     var Id = $(this).attr('id');
        //     var chgId = $(this).attr('id', Id + "1");
        //     console.log(chgId);
        // });

        // order.appendTo()

        $('#order_').clone(true).appendTo('#content_regist');

        // content_regist内のテーブル数の取得
        var num = $('#content_regist').find($('table[id^=order_]')).length;

        $('#content_regist').find('#order_, #tdCategory_, #tdGoods_, #tdNum_, #btnEdit_, #btnDel_').each(function () {
            var chgId = $(this).attr('id', $(this).attr('id') + 'add_' + num);
            var strId = chgId[0].id.split('_');

            // display noneを解除
            if (strId[0] == "order") {
                $('#' + chgId[0].id).show();
            } else if (strId[0] == "tdCategory") {
                $('#' + chgId[0].id).append(strCategory)
            } else if (strId[0] == "tdGoods") {
                $('#' + chgId[0].id).append(strGoods)
            } else if (strId[0] == "tdNum") {
                $('#' + chgId[0].id).append(strNum + "個")
            }
        });

        // 所定の要素に新たな要素とテキストを追加する
        $('#content_regist').append('<hr>');

        // 所定の要素に新たな要素とテキストを追加する
        // $('#content_regist').append(
        //     + strCategory + '</td><td>'
        //     + strGoods + '</td><td>' + strNum + '個</td></tr></table></div>');
        // 各選択を外す
        $('select').each(function () {
            $(this).children('option').removeAttr('selected'); //optionのselected要素の削除
            this.selectedIndex = 0; //selectIndexを0に設定。
        });
    });
});


function pop(self) {
    $('#imagemodal').modal('show');
};

function display_member() {
    $('#member').find('[name=member_name]').each(function (index, element) {
        if ($(element).prop("checked") && !$(element).prop("disabled")) {
            $('#search_member').append("<li id='memberId_" + $(element).attr("id") + "'>" + $(element).val() + "</li>");
            $("#" + $(element).attr("id")).prop('disabled', true);
        }
    });
};



// 登録処理
function regist(self) {
    // 入力チェック
    // TODO

    // 登録会員数取得
    var member_num = $('li[id^=memberId_]').length;

    // 登録するメニュー数の取得
    var order_num = $('#content_regist').find($('table[id^=order_]')).length;

    // 来店日
    var visit_date = $('#visit_date').val();

    // 来店人数
    var visit_num = $('#visit_num').val();

    // 注文内容の取得
    $('table[id^=order_add_]');

    // order_add_の数字の取得
    var orderNum = $('table[id^=order_add_]')[0].id;
    console.log(orderNum);
}
