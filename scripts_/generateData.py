from faker import Faker
import re
import dns.resolver


class SPFDataGenerator:
    """
        Class for generating random SPF record values using the Faker library.
    """
    def __init__(self):
        self.fake = Faker()

    def __is_domain_name_valid(self, domain):
        """
            Validates the domain name.
        """
        regex = re.compile(
            r'^(?:[a-zA-Z0-9]'  # First character of the domain
            r'(?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)'  # Sub domain + hostname
            r'+[a-zA-Z]{2,6}$'  # First level TLD
        )
        return re.match(regex, domain) is not None

    def __is_spf_record_valid(self, domain):
        """
            Checks if the domain has a valid SPF record.
        """
        try:
            answers = dns.resolver.resolve(domain, 'TXT')
            for rdata in answers:
                if any("v=spf1" in txt_string.decode() for txt_string in rdata.strings):
                    return True
            return False
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.exception.Timeout):
            return False

    def __is_ipv4_valid(self, ipv4):
        """
            Validates the IPv4 address.
        """
        regex = re.compile(
            r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$'
        )
        return re.match(regex, ipv4) is not None

    def __is_ipv6_valid(self, ipv6):
        """
            Validates the IPv6 address.
        """
        regex = re.compile(
            r'^(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}$'
        )
        return re.match(regex, ipv6) is not None

    def __is_a_record_valid(self, domain):
        """
            Checks if the domain has a valid A record.
        """
        try:
            answers = dns.resolver.resolve(domain, 'A')
            return len(answers) > 0
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.exception.Timeout):
            return False

    def __is_mx_record_valid(self, domain):
        """
            Checks if the domain has a valid MX record.
        """
        try:
            answers = dns.resolver.resolve(domain, 'MX')
            return len(answers) > 0
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.exception.Timeout):
            return False

    def generate_domain_name_value(self):
        """
            Generates a random valid domain name.
        """
        domain = self.fake.domain_name()
        return domain if self.__is_domain_name_valid(domain) else self.generate_domain_name_value()

    def generate_domain_name_without_spf(self):
        """
            Generates a random valid domain name that has no SPF records.
        """
        domain = self.fake.domain_name()
        return domain if not self.__is_spf_record_valid(domain) else self.generate_domain_name_without_spf()

    def generate_include_value(self):
        """
            Generates a random valid domain name for the include field.
        """
        domain = self.fake.domain_name()
        return domain if self.__is_spf_record_valid(domain) else self.generate_include_value()

    def generate_ipv4_value(self):
        """
            Generates a random valid IPv4 address with a subnet mask.
        """
        ipv4 = self.fake.ipv4()
        subnet = self.fake.random_element(elements=("20", "24"))
        return f"{ipv4}/{subnet}" if self.__is_ipv4_valid(ipv4) else self.generate_ipv4_value()

    def generate_ipv6_value(self):
        """
            Generates a random valid IPv6 address with a subnet mask.
        """
        ipv6 = self.fake.ipv6()
        subnet = self.fake.random_element(elements=("36", "64"))
        return f"{ipv6}/{subnet}" if self.__is_ipv6_valid(ipv6) else self.generate_ipv6_value()

    def generate_a_record_value(self):
        """
            Generates a random valid domain name for the A record.
        """
        domain = self.fake.domain_name()
        return domain if self.__is_a_record_valid(domain) else self.generate_a_record_value()

    def generate_mx_record_value(self):
        """
            Generates a random valid domain name for the MX record.
        """
        domain = self.fake.domain_name()
        return domain if self.__is_mx_record_valid(domain) else self.generate_mx_record_value()

    def generate_exists_value(self):
        """
            Generates a random valid domain name for the exists field.
        """
        domain = self.fake.domain_name()
        return f"%{{i}}._spf.{domain}" if self.__is_domain_name_valid(domain) else self.generate_exists_value()

    def generate_random_invalid_value(self, field):
        """
            Gets a random invalid value for a given field.
        """
        import random
        from testData_.data import invalidDomainNames, invalidIncludeValues, invalidIpv4Values, invalidIpv6Values, invalidARecordValues, invalidMxRecordValues, invalidExistsValues
        if field == 'domain':
            return random.choice(invalidDomainNames)
        elif field == 'include':
            return random.choice(invalidIncludeValues)
        elif field == 'ipv4':
            return random.choice(invalidIpv4Values)
        elif field == 'ipv6':
            return random.choice(invalidIpv6Values)
        elif field == 'aRecord':
            return random.choice(invalidARecordValues)
        elif field == 'mxRecord':
            return random.choice(invalidMxRecordValues)
        elif field == 'exists':
            return random.choice(invalidExistsValues)
        else:
            return None

    def generate_spf_record(self, valid=True, include=None, ipv4=None, ipv6=None, aRecord=None, aRecordOtherDomain=False, mxRecord=None, mxRecordOtherDomain=False, exists=None, failurePolicy=None):
        """
            Generates an SPF record.

            Parameters:
                - valid (bool): If True, generates a valid SPF record; if False, generates an invalid SPF record.
                - ipv4 (bool): If True, includes an IPv4 address in the SPF record.
                - ipv6 (bool): If True, includes an IPv6 address in the SPF record.
                - include (bool): If True, includes an 'include' directive in the SPF record.
                - aRecord (bool): If True, includes an 'a' directive in the SPF record.
                - aRecordOtherDomain (bool): If True, includes an 'a' directive with another domain.
                - mxRecord (bool): If True, includes an 'mx' directive in the SPF record.
                - mxRecordOtherDomain (bool): If True, includes an 'mx' directive with another domain.
                - exists (bool): If True, includes an 'exists' directive in the SPF record.
                - failurePolicy (str): Specifies the failure policy ('Fail', 'SoftFail', 'Neutral','None', or None).
            Returns:
                - str: The generated SPF record.
        """
        spfParts = ["v=spf1"]

        if include:
            spfParts.append(f"include:{self.generate_include_value() if valid else self.generate_random_invalid_value('include')}")
        if ipv4:
            spfParts.append(f"ip4:{self.generate_ipv4_value() if valid else self.generate_random_invalid_value('ipv4')}")
        if ipv6:
            spfParts.append(f"ip6:{self.generate_ipv6_value() if valid else self.generate_random_invalid_value('ipv6')}")
        if aRecord:
            if aRecordOtherDomain:
                spfParts.append(f"a:{self.generate_a_record_value() if valid else self.generate_random_invalid_value('aRecord')}")
            else:
                spfParts.append("a")
        if mxRecord:
            if mxRecordOtherDomain:
                spfParts.append(f"mx:{self.generate_mx_record_value() if valid else self.generate_random_invalid_value('mxRecord')}")
            else:
                spfParts.append("mx")
        if exists:
            spfParts.append(f"exists:{self.generate_exists_value() if valid else self.generate_random_invalid_value('exists')}")

        # Handle failure policy
        if failurePolicy == "Fail":
            spfParts.append("-all")
        elif failurePolicy == "SoftFail":
            spfParts.append("~all")
        elif failurePolicy == "Neutral":
            spfParts.append("?all")
        elif failurePolicy == "None":
            pass  # Do not append anything if "None" is explicitly given
        elif failurePolicy is None:
            spfParts.append("~all")  # Default to SoftFail if not provided
        else:
            raise ValueError(f"Invalid Failure Policy value: {failurePolicy}")

        spfRecord = " ".join(spfParts)
        return spfRecord
