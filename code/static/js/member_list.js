// $('#myform :checkbox').change(function () {
//     // チェックされたidを取得
//     var age_id = this.id;
//     // 年齢
//     var age = "";
//     // チェックボックスをクリックした時の場合分け
//     if ($(this).is(':checked')) {
//         // チェックした時
//         // id事の場合分け
//         if (age_id == "age20") {
//             // 20代の時
//             age = $('#hf_age20').val();
//         } else if (age_id == "age20") {
//             // 30代の時
//             age = $('#hf_age30').val();
//         } else if (age_id == "age20") {
//             // 40代の時
//             age = $('#hf_age40').val();
//         } else if (age_id == "age20") {
//             // 50代の時
//             age = $('#hf_age50').val();
//         } else {
//             // 60代の時
//             age = $('#hf_age60').val();
//         }
//         // チェックされたチェックボックスのvauleに値を追加
//         $('#' + age_id).val(age);
//     } else {
//         // チェックを外した時
//         if (age_id == "age20") {
//             $('#age20').val("");
//         } else if (age_id == "age20") {
//             $('#age30').val("");
//         } else if (age_id == "age20") {
//             $('#age40').val("");
//         } else if (age_id == "age20") {
//             $('#age50').val("");
//         } else {
//             $('#age60').val("");
//         }
//     }
// });
$(function () {
    $('#latest_visit_date').datepicker({
        format: 'yyyy-mm-dd',
        language: 'ja'
    });
});

$(function () {
    $('#before_visit_date').datepicker({
        format: 'yyyy-mm-dd',
        language: 'ja'
    });
});
$(function () {
    $('#after_visit_date').datepicker({
        format: 'yyyy-mm-dd',
        language: 'ja'
    });
});
var getURLParams = function (path, item) {
    if (!path) return false;

    var param = path.match(/\?([^?]*)$/);

    if (!param || param[1] === '') return false;

    var tmpParams = param[1].split('&');
    var keyValue = [];
    var params = {};
    var iIdx = 0
    for (var i = 0, len = tmpParams.length; i < len; i++) {
        keyValue = tmpParams[i].split('=');
        if (item == keyValue[0]) {
            params[iIdx] = keyValue[1];
            iIdx++
        }
    }
    return params;
};

var urlStr = location.search;

// 年齢のパラメータ取得
var resultAge = getURLParams(urlStr, "age");
// 取得したパラメータを元にチェックボックスにcheckedを追加
$.each(resultAge, function (index, value) {
    var resVal = value;
    var age = $('#myform').find('[name=age]');
    $.each(age, function (index, value) {
        if (resVal == $('#' + value.id).val()) {
            $('input[id="' + value.id + '"]').prop("checked", true);
            return false;
        }
    })
})
// 来店回数のパラメータ取得
var resultVisitNum = getURLParams(urlStr, "visitNum");
// 取得したパラメータを元にチェックボックスにcheckedを追加
$.each(resultVisitNum, function (index, value) {
    var resVal = value;
    var visitNum = $('#myform').find('[name=visitNum]');
    $.each(visitNum, function (index, value) {
        if (resVal == $('#' + value.id).val()) {
            $('input[id="' + value.id + '"]').prop("checked", true);
            return false;
        }
    })
})

var gerder = $('#tbl_list').find('[name=gender]');
$.each(gerder, function (index, value) {
    var resText = value.innerText
    if (resText == "1") {
        value.innerText = "男"
    } else if (resText == "2") {
        value.innerText = "女"
    } else if (resText == "3") {
        value.innerText = "その他"
    } else {
        value.innerText = ""
    }

    console.log(resText);
})
