def count_unread_messages(messages):
    total = messages.get("count", 0)

    for subgroup in messages.get("subgroups", []):
        total += count_unread_messages(subgroup)

    return total


# Example
chat = {
    "count": 5,
    "subgroups": [
        {
            "count": 3,
            "subgroups": []
        },
        {
            "count": 2,
            "subgroups": [
                {
                    "count": 4,
                    "subgroups": []
                }
            ]
        }
    ]
}

print("Total unread messages:", count_unread_messages(chat))
