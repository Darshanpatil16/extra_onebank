def insurance_info(policy_id, holder_name, policy_type, premium_amount):
    return (
        f"Policy ID: {policy_id}\n"
        f"Policy Holder Name: {holder_name}\n"
        f"Policy Type: {policy_type}\n"
        f"Premium Amount: {premium_amount}"
    )


if __name__ == "__main__":
    policy_id = "INS101"
    holder_name = "Darshan P"
    policy_type = "Health"
    premium_amount = 15500

    print("Insurance Details\n")
    print(insurance_info(policy_id, holder_name, policy_type, premium_amount))
