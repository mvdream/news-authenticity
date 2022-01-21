let csrftoken = $("[name=csrfmiddlewaretoken]").val();

$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
});

$(document).ready(function () {

});
function changeVoteCount(votyType, newsId, URL) {
    $.ajax({
        url: URL,
        type: "PUT",
        contentType: 'application/json',
        data: JSON.stringify({
            'voteType': votyType,
            'newsId': newsId,
        }),
        dataType: 'json',
        success: function (data) {
            alert("Thanks for Vote")
        }
    });
}