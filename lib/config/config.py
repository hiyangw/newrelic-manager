config = {
    "dashboards": {
        "functions": {
            "list": {
                "response_key": "dashboards",
                "title": "filter_title"
            },
            "show": {
                "response_key": "dashboard",
                "id": "id"
            },
            "update": {
                "response_key": "dashboard",
                "id": "id",
                "data": "dashboard_data"
            },
            "delete": {
                "response_key": "dashboard",
                "id": "id",
            },
            "create": {
                "response_key": "dashboard",
                "title": "filter_title",
                "data": "dashboard_data"
            },
            "backup": {
                "response_key": "dashboards",
                "title": "filter_title",
                "id": "id"
            },
            "restore": {
                "response_key": "dashboards",
                "id": "id"
            }
        },
        "fields": ["id", "title", "ui_url", "updated_at", "created_at"],
        "class_name": "Dashboards"
    },
    "applications": {
        "functions": {
            "list": {
                "response_key": "applications",
                "name": "filter_name",
                "id": "filter_ids",
                "language": "filter_language"
            },
            "show": {
                "response_key": "application",
                "id": "id",
            },
            "update": {
                "response_key": "application",
                "id": "id",
                "name": "name",
                "app_apdex_threshold": "app_apdex_threshold",
                "end_user_apdex_threshold": "end_user_apdex_threshold",
                "enable_real_user_monitoring": "enable_real_user_monitoring"
            },
            "delete": {
                "response_key": "application",
                "id": "id",
            },
            "metric_names": {
                "response_key": "metric",
                "id": "id",
                "name": "name"
            },
            "metric_data": {
                "response_key": "metric_data",
                "id": "id",
                "name": "name",
                "values": "values",
                "from_dt": "from",
                "to_dt": "to",
                "summarize": "summarize",
            },
            "backup": {
                "response_key": "application",
                "name": "filter_name",
                "id": "id"
            },
            "restore": {
                "response_key": "application",
                "id": "id"
            }
        },
        "fields": ["id", "name", "language", "health_status", "reporting"],
        "class_name": "Applications"
    },
    "users": {
        "functions": {
            "list": {
                "response_key": "users",
                "email": "filter_email",
                "id": "filter_ids"
            },
            "show": {
                "response_key": "user",
                "id": "id"
            }
        },
        "fields": ["id", "email", "first_name", "last_name", "role"],
        "class_name": "Users"
    },
    "alerts_policies": {
        "functions": {
            "list": {
                "response_key": "policies",
                "name": "filter_name"
            },
            "update": {
                "response_key": "policy",
                "id": "id",
                "incident": "incident_preference"
            },
            "delete": {
                "response_key": "policy",
                "id": "id",
            },
            "create": {
                "response_key": "policy",
                "name": "filter_name",
                "incident": "incident_preference"
            }
        },
        "fields": ["id", "name", "incident_preference", "updated_at", "created_at"],
        "class_name": "AlertPolicies"
    },
    "alerts_channels": {
        "functions": {
            "list": {
                "response_key": "channels"
            },
            "delete": {
                "response_key": "channel",
                "id": "id",
            },
            "create": {
                "response_key": "channel",
                "type": "type",
                "configuration": "configuration"
            }
        },
        "fields": ["id", "name", "type", "links"],
        "class_name": "NotificationChannels"
    },
    "alerts_nrql_conditions": {
        "functions": {
            "list": {
                "response_key": "nrql_conditions",
                "policy_id": "policy_id"
            },
            "show": {
                "response_key": "nrql_conditions",
                "id": "policy_id"
            },
            "delete": {
                "response_key": "nrql_condition",
                "id": "id",
            },
            "update": {
                "response_key": "nrql_condition",
                "alert_condition_nrql_id": "alert_condition_nrql_id",
                "policy_id": "policy_id",
                "data": "data"
            },
            "create": {
                "response_key": "nrql_condition",
                "policy_id": "policy_id",
                "data": "data"
            },
            "backup": {
                "response_key": "nrql_conditions",
                "id": "id"
            },
            "restore": {
                "response_key": "nrql_conditions",
                "id": "id"
            }
        },
        "fields": ["id", "name", "type", "links"],
        "class_name": "AlertConditionsNRQL"
    },
}
