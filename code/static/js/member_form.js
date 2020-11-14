
$(function () {
    $('#button').on('click', function () {

        const name = $('#name').val();
        const name_read = $('#name_read').val();
        const gender = $('option:selected').val();
        const age = $('#age').val();
        const birthday = $('#year').val() + "-" + $('#month').val() + "-" + $('#day').val();
        const zip_code = $('#zipCode1').val() + "-" + $('#zipCode2').val();
        const prefectures = $('#prefectures').val();
        const address1 = $('#address1').val();
        const address2 = $('#address2').val();
        const house = $('#house').val();
        const telephone = $('#telephone').val();
        const email = $('#email').val();
        const remark = $('#remark').val();

        $('#id_name').val(name);
        $('#id_name_read').val(name_read);
        $('#id_gender').val(gender)
        $('#id_age').val(age);
        $('#id_birth_day').val(birthday);
        $('#id_zip_code').val(zip_code);
        $('#id_prefectures').val(prefectures);
        $('#id_address_line1').val(address1);
        $('#id_address_line2').val(address2);
        $('#id_house').val(house);
        $('#id_telephone').val(telephone);
        $('#id_email').val(email);
        $('#id_remark').val(remark);

    });
});



// 住所検索ボタンイベント
$(function () {
    $('#searchBtn').on('click', function () {
        // 郵便番号を取得
        const zip_code_1 = $('#zipCode1').val();
        const zip_code_2 = $('#zipCode2').val();

        // 郵便番号が入力されているか場合分け
        if (zip_code_1 != "" && zip_code_2 != "") {
            // 郵便番号
            var zip_code = zip_code_1 + zip_code_2;
            // 入力されている場合
            get_address(zip_code);
        } else {
            // 入力されていない場合
            // エラーメッセージ表示
            alert("郵便番号を入力してください");
        }
    });
});

// 住所検索web_apiを叩く
//Ajax関数
function get_address(val) {
    //入力値をセット
    var param = { zipcode: val }
    //zipcloudのAPIのURL
    var send_url = 'https://zipcloud.ibsnet.co.jp/api/search';
    $.ajax({
        type: 'GET',
        cache: false,
        data: param,
        url: send_url,
        dataType: 'jsonp',
        success: function (res) {
            //結果によって処理を振り分ける
            if (res.status == 200) {
                //処理が成功したとき
                //該当する住所を表示
                var html = '';
                for (var i = 0; i < res.results.length; i++) {
                    var result = res.results[i];
                    console.log(res.results);
                    // 都道府県
                    var strPrefectures = result.address1;
                    var strAddress1 = result.address2;
                    var strAddress2 = result.address3;
                    $('#prefectures').val(strPrefectures);
                    $('#address1').val(strAddress1);
                    $('#address2').val(strAddress2);
                }
            } else {
                //エラーだった時
                //エラー内容を表示
                $('#zip_result').html(res.message);

            }
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            console.log(XMLHttpRequest);
        }
    });
};

