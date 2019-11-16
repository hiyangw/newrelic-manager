schema = {
    "dashboards": {
        "metadata": {
            "version": 1
        },
        "title": "Dashboard Sample",
        "icon": "none|archive|bar-chart|line-chart|bullseye|user|usd|money|thumbs-up|thumbs-down|cloud|bell|bullhorn|comments-o|envelope|globe|shopping-cart|sitemap|clock-o|crosshairs|rocket|users|mobile|tablet|adjust|dashboard|flag|flask|road|bolt|cog|leaf|magic|puzzle-piece|bug|fire|legal|trophy|pie-chart|sliders|paper-plane|life-ring|heart",
        "visibility": "owner|all",
        "editable": "read_only|editable_by_owner|editable_by_all",
        "widgets": [
            {
                "visualization": "string",
                "data": [
                    {
                        "nrql": "string"
                    }
                ],
                "presentation": {
                    "title": "string",
                    "notes": "string"
                },
                "layout": {
                    "width": 1,
                    "height": 1,
                    "row": 1,
                    "column": 1
                }
            }
        ]
    },
    "applications": {}
}
