# EasyDMARC main page URL
mainPageUrl = "https://easydmarc.com/"

# EasyDMARC SPF Record tools URL
spfRecordCheckerPageUrl = "https://easydmarc.com/tools/spf-lookup"
spfRecordGeneratorPageUrl = "https://easydmarc.com/tools/spf-record-generator"
spfRecordValidatorPageUrl = "https://easydmarc.com/tools/spf-record-raw-check-validate"

# SPF Record Statuses
successStatus = "Valid"
failStatus = "Invalid"

# SPF record version value syntax and type.
spfRecordVersion = "v=spf1"
spfRecordType = "TXT"

# Failure policy values
noneValue1 = "all"
noneValue2 = "+all"
failValue = "-all"
softFailValue = "~all"
neutralValue = "?all"

# SPF record invalid data
invalidDomainNames = [
    "invalid_domain",  # Missing TLD
    "example..com",    # Double dot
    "-example.com",    # Leading hyphen
    "example-.com"     # Trailing hyphen
]
invalidIncludeValues = [
    "invalid-domain.com",
    "999.999.999.999",  # Invalid IP
    "nonexistent-domain.com",
    "abcd:1234::5678::"  # Invalid IPv6
]
invalidIpv4Values = [
    "256.256.256.256",  # Out of range
    "192.168.1",        # Incomplete
    "192.168.1.999",    # Out of range
    "192.168.1.1.1"     # Too many octets
]
invalidIpv6Values = [
    "12345::",          # Too many digits
    "abcd:1234::5678::",  # Double "::"
    "abcd:1234:5678:9abc:defg::1",  # Invalid character 'g'
    "abcd:1234:5678:9abc:def::1::"  # Double "::" at the end
]
invalidARecordValues = [
    "no-such-domain.com",
    "invalid.a.record",
    "nonexistentdomain.xyz",
    "fake-domain.test"
]
invalidMxRecordValues = [
    "no-mx-record.com",
    "invalid.mx.record",
    "nonexistent-mx.xyz",
    "fake-mx.test"
]
invalidExistsValues = [
    "invalid-domain.com",  # Nonexistent domain
    "fake-domain.test",    # Fake domain
    "nonexistent.xyz",     # Nonexistent TLD
    "invalid.exists"       # Invalid format
]

# Domain Name field validation messages
validationMessageForInvalidData = "Please provide a valid domain"
validationMessageForEmptyData = "This value is required."