// absences/form.js

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
    $('[id^=id_additional_recipients_]').each(function (element) {
        $(this).parent().html($(this).parent().html().replace('&lt;b&gt;', '<b>').replace('&lt;/b&gt;', '</b>'));
    });

    // Validation: fill summary (modal) on validation:
    $('#ticket_validation').click(function () {
        // Monks:
        let monks = "";
        $("input[id^='id_monks']:checked").each(function (i, monk) {
            monks += $(this).parent().text();
        });
        $('#monks').html(monks);

        // Destination:
        $('#destination').html($("#id_destination").val());

        // Go:
        let go = "";
        const go_date = date_to_french_string(
            string_to_date_object($("#id_go_date").val())
        );
        const go_moment = $("#id_go_moment").val().toLowerCase();
        let go_by = '';
        if ($("#id_go_by").val() != '') {
            go_by = '</br> En ' + $("#id_go_by").val().toLowerCase();
        }
        let go_train = '';
        if ($("#id_go_by").val() == 'Train') {
            const go_station = $("#id_go_station").val() == '' ? '' : ' : ' + $("#id_go_station").val();
            const go_hour = $("#id_go_hour").val() == '' ? '' : ' à ' + $("#id_go_hour").val();
            go_train = go_station + go_hour;
        }
        const go_servants = $("#id_servants").is(':checked') ? '</br>Repas avec les serveurs' : '';
        const go_picnic = $("#id_picnic").is(':checked') ? '</br>Casse-croûte' : '';
        go = go_date + ' (' + go_moment + ') ' + go_by + go_train + go_servants + go_picnic;
        $('#go').html(go);

        // Back:
        let back = "";
        const back_date = date_to_french_string(
            string_to_date_object($("#id_back_date").val())
        );
        const back_moment = $("#id_back_moment").val().toLowerCase();
        let back_by = '';
        if ($("#id_back_by").val() != '') {
            back_by = '</br> En ' + $("#id_back_by").val().toLowerCase();
        }
        let back_train = '';
        if ($("#id_back_by").val() == 'Train') {
            const back_station = $("#id_back_station").val() == '' ? '' : ' : ' + $("#id_back_station").val();
            const back_hour = $("#id_back_hour").val() == '' ? '' : ' à ' + $("#id_back_hour").val();
            back_train = back_station + back_hour;
        }
        const back_keep_hot = $("#id_keep_hot").is(':checked') ? '</br>Garder du chaud' : '';
        back = back_date + ' (' + back_moment + ') ' + back_by + back_train + back_keep_hot;
        $('#back').html(back);

        // Forme ordinaire:
        $('#ordinary').html(
            $("#id_ordinary_form").is(':checked')
                .toString()
                .replace('true', 'Oui').replace('false', 'Non')
        );

        // Commentaire:
        $('#comment').html($("#id_commentary").html().replace(/\n/g, '</br>'));

        // Destinataires obligatoires:
        $('#mandatory').html($(".recipients").html().replace(/<b>/g, '').replace(/<\/b>/g, ''));

        // Destinataires supplémentaires:
        let additionals = "";
        $("input[id^='id_additional_recipients']:checked").each(function (i, additional) {
            additionals += $(this).parent().text().replace(/\n /, '') + '</br>';
        });
        $('#additional').html(additionals);
    });
});
