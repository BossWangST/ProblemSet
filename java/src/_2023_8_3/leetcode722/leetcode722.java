package _2023_8_3.leetcode722;

import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

class Solution {
    public List<String> removeComments(String[] source) {
        var res = new ArrayList<String>();
        // Pattern line = Pattern.compile("(.*?)//.*$");
        // Pattern block_line = Pattern.compile("(.*?)/\\*.*\\*/(.*?)$");
        // Pattern block1 = Pattern.compile("(.*?)/\\*.*$");
        // Pattern block2 = Pattern.compile(".*?\\*/(.*?)$");
        /*
        Matcher m;
        for (int i = 0; i < source.length; i++) {
            String cur = source[i];
            Matcher m1 = line.matcher(cur);
            Matcher m2 = block_line.matcher(cur);
            if (m1.find() && m2.find()) {
                Boolean line_or_block = true;
                for (int j = 0; j < cur.length() - 1; j++) {
                    if (cur.startsWith("//", j))
                        break;
                    if (cur.startsWith("/*", j))
                        line_or_block = false;
                }
                if (line_or_block) {
                    // line
                    m = line.matcher(cur);
                    if (m.find()) {
                        cur = m.group(1);
                        if (cur.equals(""))
                            continue;
                    }
                    // block line
                    m = block_line.matcher(cur);
                    if (m.find()) {
                        cur = m.group(1) + m.group(2);
                        if (cur.equals(""))
                            continue;
                    }
                } else {
                    // block line
                    m = block_line.matcher(cur);
                    if (m.find()) {
                        cur = m.group(1) + m.group(2);
                        if (cur.equals(""))
                            continue;
                    }
                    // line
                    m = line.matcher(cur);
                    if (m.find()) {
                        cur = m.group(1);
                        if (cur.equals(""))
                            continue;
                    }
                }
            } else {
                // block line
                m = block_line.matcher(cur);
                if (m.find()) {
                    cur = m.group(1) + m.group(2);
                    if (cur.equals(""))
                        continue;
                }
                // line
                m = line.matcher(cur);
                if (m.find()) {
                    cur = m.group(1);
                    if (cur.equals(""))
                        continue;
                }
            }
            // block
            m = block1.matcher(cur);
            if (m.find()) {
                cur = m.group(1);
                String left = "";
                if (!cur.equals(""))
                    left = cur;
                while (++i < source.length) {
                    m = block2.matcher(source[i]);
                    if (m.find()) {
                        cur = m.group(1);
                        // block line
                        m = block_line.matcher(cur);
                        if (m.find()) {
                            cur = m.group(1) + m.group(2);
                            if (cur.equals(""))
                                break;
                        }
                        // line
                        m = line.matcher(cur);
                        if (m.find()) {
                            cur = m.group(1);
                            if (cur.equals(""))
                                break;
                        }
                        cur = left + cur;
                        if (cur.equals(""))
                            break;
                        res.add(cur);
                        break;
                    }
                }
                continue;
            }
            res.add(cur);
        }
        */
        Boolean block = false;
        StringBuilder cur = new StringBuilder();
        for (String s : source) {
            int n = s.length();
            for (int i = 0; i < n; i++) {
                if (block) {
                    if (i + 1 < n && s.charAt(i) == '*' && s.charAt(i + 1) == '/') {
                        block = false;
                        i++;
                    }
                } else {
                    if (i + 1 < n && s.charAt(i) == '/' && s.charAt(i + 1) == '*') {
                        block = true;
                        i++;
                    } else if (i + 1 < n && s.charAt(i) == '/' && s.charAt(i + 1) == '/')
                        break;
                    else
                        cur.append(s.charAt(i));
                }
            }
            if (!block && cur.length() > 0) {
                res.add(cur.toString());
                cur.setLength(0);
            }
        }
        return res;
    }
}

public class leetcode722 {
    public static void main(String[] args) {
        var s = new Solution();
        var res = s.removeComments(new String[]{"a/*/b//*c", "blank", "d/*/e*//f"});
        for (String str : res)
            System.out.println(str);
    }
}
