/**
 * Created by: danigosa
 * Override default zinnia template for support modeltranslation
 * Infantium.com
 */

$(document).ready(function() {
    $("#id_content_en").wymeditor({
        skin: "django", lang: "{{ lang }}",
        stylesheet: "{{ STATIC_URL }}zinnia/css/wymeditor_styles.css",
        updateSelector: "input:submit", updateEvent: "click",
        postInit: function(wym) {
            wym.hovertools();
        }
    });
    $("#id_content_es").wymeditor({
        skin: "django", lang: "{{ lang }}",
        stylesheet: "{{ STATIC_URL }}zinnia/css/wymeditor_styles.css",
        updateSelector: "input:submit", updateEvent: "click",
        postInit: function(wym) {
            wym.hovertools();
        }
    });
});