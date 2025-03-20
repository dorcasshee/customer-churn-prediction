def validate(input_dict):
    errors = []
    required_fields = ['age', 'senior_citizen', 'married', 'num_dependents', 'tenure_months', 'num_referrals', 'paperless_billing', 
                       'has_internet_service', 'has_premium_tech_support', 'has_unlimited_data', 'total_monthly_fee', 'total_charges_quarter',
                       'avg_long_distance_fee_monthly', 'avg_gb_download_monthly']
    
    for field in required_fields:

        if field not in input_dict:
            errors.append(f'The {field} field is missing. Please enter the appropriate value.')
            
        elif field in ['age', 'num_dependents', 'tenure_months', 'num_referrals', 'avg_gb_download_monthly'] \
            and type(input_dict[field]) != int and isinstance(input_dict[field], int):
            errors.append(f'The {field} field must be an integer.')

        elif field in ['total_monthly_fee', 'total_charges_quarter', 'avg_long_distance_fee_monthly'] and\
            type(input_dict[field]) != float and isinstance(input_dict[field], float):
            try:
                float(input_dict[field])
            except ValueError:
                errors.append(f'The {field} field must be numeric.')
        
    if int(input_dict['age']) < 65 and input_dict['senior_citizen'] == 'yes':
        errors.append('Senior citizens must be at least 65 years old and above.')
    elif int(input_dict['age']) >= 65 and input_dict['senior_citizen'] == 'no':
        errors.append('Those aged 65 years and above qualify as senior citizens.')

    return errors

def format_model_inputs(input_dict):
    binary_inputs = ['senior_citizen', 'married', 'paperless_billing', 'has_internet_service', 'has_unlimited_data', 'has_premium_tech_support']
    
    for input in binary_inputs:
        if input_dict[input] == "no": input_dict[input] = 0
        if input_dict[input] == "yes": input_dict[input] = 1
    
    age = int(input_dict['age'])
    senior_citizen = int(input_dict['senior_citizen'])
    married = int(input_dict['married'])
    num_dependents = int(input_dict['num_dependents'])
    tenure_months = int(input_dict['tenure_months'])
    num_referrals = int(input_dict['num_referrals'])
    paperless_billing = input_dict['paperless_billing']
    has_internet_service = int(input_dict['has_internet_service'])
    has_unlimited_data = int(input_dict['has_unlimited_data'])
    has_premium_tech_support = int(input_dict['has_premium_tech_support'])
    total_monthly_fee = float(input_dict['total_monthly_fee'])
    total_charges_quarter = float(input_dict['total_charges_quarter'])
    avg_long_distance_fee_monthly = float(input_dict['avg_long_distance_fee_monthly'])
    avg_gb_download_monthly = int(input_dict['avg_gb_download_monthly'])
    
    return [age, senior_citizen, married, num_dependents, tenure_months, num_referrals, paperless_billing, has_internet_service, 
            has_premium_tech_support, has_unlimited_data, total_monthly_fee, total_charges_quarter, avg_long_distance_fee_monthly, 
            avg_gb_download_monthly]