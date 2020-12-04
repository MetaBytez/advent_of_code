# https://adventofcode.com/2020/day/4
import re


class Passport:
    REQUIRED_FIELDS = {
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
    }

    OPTIONAL_FIELDS = {
        'cid',
    }

    VALID_HAIR_COLORS = {
        'amb',
        'blu',
        'brn',
        'gry',
        'grn',
        'hzl',
        'oth'
    }

    def __init__(self, passport_data: str):
        self.passport_data = {}
        self.has_required_fields = False
        self.valid = False

        missing_fields = set(self.REQUIRED_FIELDS)
        invalid_fields = set(self.REQUIRED_FIELDS)

        for datum in passport_data.split():
            field, val = datum.split(':')
            missing_fields.discard(field)
            self.passport_data[field] = val
            if self.valid_field(field):
                invalid_fields.discard(field)

        if not missing_fields:
           self.has_required_fields = True

        if not invalid_fields:
            self.valid = True

    def __str__(self) -> str:
        # This order puts the variable with items at the end of the line
        order = ['byr','iyr','eyr','hcl','ecl','pid', 'hgt', 'cid']
        sorted_data = {
            field: self.passport_data.get(field, None)
            for field in order
        }
        return str(sorted_data)

    def valid_field(self, field_name: str) -> bool:
        """Determines if a given field is valid for this passport"""
        field_val = self.passport_data.get(field_name)

        if field_val is None and field_name not in self.OPTIONAL_FIELDS:
            return False
        elif field_name == 'byr':
            return 1920 <= int(field_val) <= 2002
        elif field_name == 'iyr':
            return 2010 <= int(field_val) <= 2020
        elif field_name == 'eyr':
            return 2020 <= int(field_val) <= 2030
        elif field_name == 'hgt':
            if 'cm' in field_val:
                return 150 <= int(field_val[:-2]) <= 193
            elif 'in' in field_val:
                return 59 <= int(field_val[:-2]) <= 76
            else:
                return False
        elif field_name == 'hcl':
            return re.match(r'#[a-f0-9]{6}$', field_val) is not None
        elif field_name == 'ecl':
            return field_val in self.VALID_HAIR_COLORS
        elif field_name == 'pid':
            return re.match(r'\d{9}$', field_val) is not None


def part_1() -> int:
    """260"""
    num_valid = 0

    with open('input.txt') as f:
        for datum in f.read().split('\n\n'):
            if Passport(datum.replace('\n', ' ')).has_required_fields:
                num_valid += 1
    
    return num_valid


def part_2() -> int:
    """153"""
    num_valid = 0

    with open('input.txt') as f:
        for datum in f.read().split('\n\n'):
            passport = Passport(datum.replace('\n', ' '))
            if passport.valid:
                num_valid += 1
    
    return num_valid


if __name__ == '__main__':
    print(part_1())
    print(part_2())
