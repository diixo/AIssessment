
"Assistant: Hi, I am development assistant. Do you have any assigned tickets on you?"

"User: No"

"Assistant: you should ask your Line Manager to assign task on you, or create new one by yourself."

"User: Yes"

"Assistant: what is number or ID?"

workflow = {

    "State":
    {
        "JUST REGISTERED": [ "To Blocked", "To Suspended", "To Do" ],
        "TO DO": [ "To Blocked", "To Suspended", "To Implement", "To Under Verification", ],
        "IMPLEMENTATION": [ "To Blocked", "To Suspended", "To Under Verification", "To Test", "To Do", ],
        "IN SW TESTING": [ "To Blocked", "To Suspended", "To Integrate" ],
        "IN SYSTEM INTEGRATION": [ "To Blocked", "To Suspended", "To Verification" ],
        "UNDER VERIFICATION": [ "To Blocked", "To Suspended", "Fixes Needed", "Close ADMIN", ],
        "BLOCKED": [
            "Back To Do",
            "Back to Just Registered",
            "Back to Under Verification",
            "Back to SW Testing",
            "Back to System Integration",
            "Back to Implementation",
            ],
        "SUSPENDED": [
            "Back To Do",
            "Back to Implementation",
            "Back to Under Verification",
            "Back to Just Registered",
            "Back to SW Testing",
            "Back to System Integration"
            ],

        "CLOSED": [ "To Blocked", "Reopen", ],
    },
    "Transition":
    {
        "To Implement": "IMPLEMENTATION",
        "Fixes Needed": "IMPLEMENTATION",
        "Back to Implementation": "IMPLEMENTATION",
        "Back To Do": "TO DO",
        "To Under Verification": "UNDER VERIFICATION",
        "Back to Under Verification": "UNDER VERIFICATION",
        "To Just Registered": "JUST REGISTERED",
        "Create": "JUST REGISTERED",
        "Back to Just Registered": "JUST REGISTERED",
        "Reopen": "JUST REGISTERED",
        "Back to SW Testing": "IN SW TESTING",
        "Back to System Integration": "IN SYSTEM INTEGRATION",
        "To Integrate": "IN SYSTEM INTEGRATION",
        "To Test": "IN SW TESTING",
        "To Blocked": "BLOCKED",
        "To Suspended": "SUSPENDED",
        "To Verification": "UNDER VERIFICATION",
        "Close ADMIN": "CLOSED",
        "To Do": "TO DO",
    }
}
