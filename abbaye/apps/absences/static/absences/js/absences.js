$(document).ready(function () {
    // Voiture/train: on change, display or hide group_train:
    $("#id_go_by").change(function () {
        if ($("#id_go_by option:selected").text() == "Train") {
            $("#group_train_go").attr("class", "d-flex");
        } else {
            $("#group_train_go").attr("class", "d-none");
        }
    }).trigger('change');
    $("#id_back_by").change(function () {
        if ($("#id_back_by option:selected").text() == "Train") {
            $("#group_train_back").attr("class", "d-flex");
        } else {
            $("#group_train_back").attr("class", "d-none");
        }
    }).trigger('change');

    // Checkbox all additional recipients:
    $('#checkbox_all_additional_recipients').click(function () {
        if ($(this).prop('checked')) {
            $('#id_additional_recipients').find(':checkbox').each(function () {
                $(this).prop('checked', true);
            })
        }
        else {
            $('#id_additional_recipients').find(':checkbox').each(function () {
                $(this).prop('checked', false);
            })
        }
    });

    // Additional recipients: set name in bold:
    $("[id^=id_additional_recipients_]").each(function (element) {
        $(this).parent().html($(this).parent().html().replace('&lt;b&gt;', '<b>').replace('&lt;/b&gt;', '</b>'));
    });
});
