from insurance import insurance_info

def test_insurance_info():
    expected_output = (
        "Policy ID: INS101\n"
        "Policy Holder Name: Darshan P\n"
        "Policy Type: Health\n"
        "Premium Amount: 15500"
    )

    result = insurance_info("INS101", "Darshan P", "Health", 15500)
    assert result == expected_output
