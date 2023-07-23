import re
import collections


def cal(formula, atom, rate):
    alphabet = '[A-Z][a-z]*'
    number = '[0-9]*'
    plain = '(.*?)\('
    while len(formula) > 0:
        if formula[0] == '(':
            i = 0
            left = 1
            while left > 0:
                if formula[i + 1] == '(':
                    left += 1
                elif formula[i + 1] == ')':
                    left -= 1
                i += 1
            process = formula[1:i]
            formula = formula[i + 1:]
            num = re.match(number, formula).group(0)
            formula = formula[len(num):]
            if len(num) == 0:
                cal(process, atom, rate*1)
            else:
                num = (int)(num)
                cal(process, atom, rate*(int)(num))
        else:
            process_re = re.match(plain, formula)
            if process_re is not None:
                process = process_re.group(1)
                formula = formula[len(process):]
            else:
                process = formula
                formula = ''
            while len(process) > 0:
                atom_name = re.match(alphabet, process).group(0)
                process = process[len(atom_name):]
                atom_num = re.match(number, process).group(0)
                process = process[len(atom_num):]
                if atom_num == '':
                    atom_num = 1 * rate
                else:
                    atom_num = int(atom_num) * rate
                if atom_name not in atom:
                    atom[atom_name] = atom_num
                else:
                    atom[atom_name] += atom_num


class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        atom = {}
        cal(formula, atom, 1)
        atom = collections.OrderedDict(sorted(atom.items()))
        res = ''
        for i in atom:
            if atom[i] == 1:
                res += str(i)
            else:
                res += str(i) + str(atom[i])
        return res


s = Solution()
print(s.countOfAtoms('K4(ON(SO3)2)2'))
