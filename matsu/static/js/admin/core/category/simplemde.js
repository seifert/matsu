window.onload = function() {
    var content_mde = new SimpleMDE({
        autosave: {
            enabled: false,
            uniqueId: "matsu-admin-category-content",
        },
        element: document.getElementById("id_content"),
        forceSync: true,
        hideIcons: [
            "heading", "heading-smaller", "heading-bigger", "heading-1",
            "heading-2", "code", "clean-block", "table", "side-by-side",
            "fullscreen"
        ],
        indentWithTabs: false,
        lineWrapping: true,
        showIcons: [
            "bold", "italic", "strikethrough", "heading-3", "quote",
            "unordered-list", "ordered-list", "link", "image",
            "horizontal-rule", "preview", "guide"
        ],
        spellChecker: false,
        status: false
    });
}
