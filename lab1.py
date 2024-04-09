rubrics1 = r"""
- points: 0
  cmd: "lab1_part1"
  expect: "1"
  note: "[Getppid] Get ppid failed"
  name: "Getppid - fail"

- points: 15
  expect: "0"
  note: "[Getppid] Get ppid succeeded"
  name: "Getppid - successful"
"""


rubrics23 = r"""
- points: 5
  cmd: "lab1_part23 1"
  expect: "4 0"
  note: "Fork failed"
  name: "Exit & Wait - Fork first child process"

- points: 5
  expect: "4+0"
  note: "[Exit & Wait]Failed to obtain correct first child process exit status"
  name: "Exit & Wait - Wait for first child process"

- points: 0
  expect: "5 -1"
  note: "[Exit & Wait]Fork second child process failed"
  name: "Exit & Wait - Fork second child process"

- points: 15
  expect: "5+-1"
  note: "[Exit & Wait]Failed to obtain correct second child process exit status"
  name: "Exit & Wait - Wait for second child process"

- points: 5
  cmd: "lab1_part23 2"
  expect: "-1 -1"
  note: "[Exit & Wait]Should return -1 for a child process that does not exist"
  name: "Exit & Wait - Wait for a child process that does not exist"

"""

code1 = """I2luY2x1ZGUgInR5cGVzLmgiCiNpbmNsdWRlICJ1c2VyLmgiCgp2b2lkIGdldFBhcmVudCh2b2lkKXsKICAgIGludCBwaWQgPSBnZXRwaWQoKTsKICAgIGludCByZXQgPSBmb3JrKCk7CiAgICBpZihyZXQgPT0gMCl7CiAgICAgICAgaW50IHBwaWRfY2hpbGQgPSBnZXRwcGlkKCk7CiAgICAgICAgaWYgKHBpZCA9PSBwcGlkX2NoaWxkKXsKICAgICAgICAgICAgcHJpbnRmKDEsICIlZFxuIiwgMCk7CiAgICAgICAgfQogICAgICAgIGVsc2V7CiAgICAgICAgICAgIHByaW50ZigxLCAiJWRcbiIsIDEpOwogICAgICAgIH0KICAgIH0KICAgIGVsc2UgaWYgKHJldCA+IDApIHsKICAgICAgICBzbGVlcCgxKTsKICAgICAgICByZXR1cm47CiAgICB9CiAgICBlbHNlewogICAgICAgIHByaW50ZigyLCAiXG5FcnJvciB1c2luZyBmb3JrXG4iKTsKICAgIH0KfQoKaW50IG1haW4oaW50IGFyZ2MsIGNoYXIgKmFyZ3ZbXSkKewogICAgcHJpbnRmKDEsICJcbmxhYjEgcGFydDE6IHRlc3QgZ2V0cHBpZFxuIik7CiAgICBnZXRQYXJlbnQoKTsKICAgIC8vIGV4aXQoKTsKfQ=="""
# updated test code for getsiblings
code1 = """I2luY2x1ZGUgInR5cGVzLmgiCiNpbmNsdWRlICJ1c2VyLmgiCgp2b2lkIGdldFBhcmVudCh2b2lk
KXsKICAgIGludCBwaWQxLCBwaWQyOwogICAgcGlkMSA9IGZvcmsoKTsKICAgIGlmIChwaWQxID09
IDApIHsKICAgICAgICBzbGVlcCgxMCk7CiAgICB9IGVsc2UgewogICAgICAgIHBpZDIgPSBmb3Jr
KCk7CiAgICAgICAgaWYgKHBpZDIgPT0gMCkgewogICAgICAgICAgICAvLyBjaGVjayBpZiB0aGUg
c2libGluZyBpcyBwaWQxCiAgICAgICAgICAgIC8vIHByaW50ZigxLCAiZ2V0c2libGluZ3MgcGlk
ICVkXG4iLCBnZXRzaWJsaW5ncygpKTsKICAgICAgICAgICAgaWYgKHBpZDEgPT0gZ2V0c2libGlu
Z3MoKSkgewogICAgICAgICAgICAgICAgcHJpbnRmKDEsICIlZFxuIiwgMCk7CiAgICAgICAgICAg
IH0gZWxzZSB7CiAgICAgICAgICAgICAgICBwcmludGYoMSwgIiVkXG4iLCAxKTsKICAgICAgICAg
ICAgfQogICAgICAgIH0KICAgIH0KICAgIHdhaXQoMCk7CiAgICB3YWl0KDApOwogICAgcmV0dXJu
Owp9CgppbnQgbWFpbihpbnQgYXJnYywgY2hhciAqYXJndltdKQp7CiAgICAvLyBwcmludGYoMSwg
IlxubGFiMSBwYXJ0MTogdGVzdCBnZXRzaWJsaW5nc1xuIik7CiAgICBnZXRQYXJlbnQoKTsKICAg
IGV4aXQoMCk7CiAgICAvLyByZXR1cm4gMDsKfQ=="""
code23 = """I2luY2x1ZGUgInR5cGVzLmgiCiNpbmNsdWRlICJ1c2VyLmgiCgojZGVmaW5lIFdOT0hBTkcgCTEKCmludCBtYWluKGludCBhcmdjLCBjaGFyICphcmd2W10pCnsKICAgIGludCBleGl0V2FpdCh2b2lkKTsKICAgIGludCB3YWl0Tm90aGluZyh2b2lkKTsKCiAgICBwcmludGYoMSwgIlxubGFiIzFcbiIpOwogICAgaWYgKGF0b2koYXJndlsxXSkgPT0gMSkKICAgICAgICBleGl0V2FpdCgpOyAgCiAgICBlbHNlIGlmIChhdG9pKGFyZ3ZbMV0pID09IDIpCiAgICAgICAgd2FpdE5vdGhpbmcoKTsKICAgIC8vIEVuZCBvZiB0ZXN0CiAgICAvLyBleGl0KDApOwogICAgcmV0dXJuIDA7Cn0KCgppbnQgd2FpdE5vdGhpbmcodm9pZCl7CiAgICBpbnQgcmV0LCBleGl0X3N0YXR1cyA9IC0xOwogICAgcmV0ID0gd2FpdCgmZXhpdF9zdGF0dXMpOwogICAgcHJpbnRmKDEsICIlZCAlZFxuIiwgcmV0LCBleGl0X3N0YXR1cyk7CiAgICByZXR1cm4gMDsKfQoKaW50IGV4aXRXYWl0KHZvaWQpIHsKICAgIGludCBwaWQsIHJldF9waWQsIGV4aXRfc3RhdHVzOwogICAgaW50IGk7CiAgICAvLyB1c2UgdGhpcyBwYXJ0IHRvIHRlc3QgZXhpdChpbnQgc3RhdHVzKSBhbmQgd2FpdChpbnQqIHN0YXR1cykKCiAgICAvLyAgIHByaW50ZigxLCAiXG4gIFBhcnRzIGEgJiBiKSB0ZXN0aW5nIGV4aXQoaW50IHN0YXR1cykgYW5kIHdhaXQoaW50KiBzdGF0dXMpOlxuIik7CgogICAgZm9yIChpID0gMDsgaSA8IDI7IGkrKykgewogICAgICAgIHBpZCA9IGZvcmsoKTsKICAgICAgICBpZiAocGlkID09IDApIHsgLy8gb25seSB0aGUgY2hpbGQgZXhlY3V0ZWQgdGhpcyBjb2RlCiAgICAgICAgICAgIGlmIChpID09IDApewogICAgICAgICAgICAgICAgcHJpbnRmKDEsICIlZCAlZFxuIiwgZ2V0cGlkKCksIDApOwogICAgICAgICAgICAgICAgZXhpdCgwKTsKICAgICAgICAgICAgfQogICAgICAgICAgICBlbHNlewogICAgICAgICAgICAgICAgcHJpbnRmKDEsICIlZCAlZFxuIiAsZ2V0cGlkKCksIC0xKTsKICAgICAgICAgICAgICAgIGV4aXQoLTEpOwogICAgICAgICAgICB9IAogICAgICAgIH0gZWxzZSBpZiAocGlkID4gMCkgeyAvLyBvbmx5IHRoZSBwYXJlbnQgZXhlY3V0ZXMgdGhpcyBjb2RlCiAgICAgICAgICAgIHJldF9waWQgPSB3YWl0KCZleGl0X3N0YXR1cyk7CiAgICAgICAgICAgIHByaW50ZigxLCAiJWQrJWRcbiIsIHJldF9waWQsIGV4aXRfc3RhdHVzKTsKICAgICAgICB9IGVsc2UgeyAvLyBzb21ldGhpbmcgd2VudCB3cm9uZyB3aXRoIGZvcmsgc3lzdGVtIGNhbGwKICAgICAgICAgICAgcHJpbnRmKDIsICJcbkVycm9yIHVzaW5nIGZvcmtcbiIpOwogICAgICAgICAgICBleGl0KC0xKTsKICAgICAgICB9CiAgICB9CiAgICByZXR1cm4gMDsKfQoK"""
#code = """I2luY2x1ZGUgInR5cGVzLmgiCiNpbmNsdWRlICJ1c2VyLmgiCgojZGVmaW5lIFdOT0hBTkcgCTEKCmludCBtYWluKGludCBhcmdjLCBjaGFyICphcmd2W10pCnsKCWludCBnZXRQYXJlbnQodm9pZCk7CglpbnQgZXhpdFdhaXQodm9pZCk7CglpbnQgd2FpdFBpZCh2b2lkKTsKICBpbnQgd2FpdE5vdGhpbmcodm9pZCk7CgogIHByaW50ZigxLCAiXG5sYWIjMVxuIik7CiAgaWYgKGF0b2koYXJndlsxXSkgPT0gMikKCSAgd2FpdFBpZCgpOwogIGVsc2UgaWYgKGF0b2koYXJndlsxXSkgPT0gMSkKICAgIGV4aXRXYWl0KCk7ICAKICBlbHNlIGlmIChhdG9pKGFyZ3ZbMV0pID09IDMpCiAgICB3YWl0Tm90aGluZygpOwogICAgLy8gRW5kIG9mIHRlc3QKCSBleGl0KDApOwoJIHJldHVybiAwOwogfQogIGludCB3YWl0Tm90aGluZyh2b2lkKXsKICAgIGludCByZXQsIGV4aXRfc3RhdHVzID0gLTE7CiAgICByZXQgPSB3YWl0KCZleGl0X3N0YXR1cyk7CiAgICBwcmludGYoMSwgIiVkICVkXG4iLCByZXQsIGV4aXRfc3RhdHVzKTsKICAgIHJldHVybiAwOwogfQoKaW50IGV4aXRXYWl0KHZvaWQpIHsKCSAgaW50IHBpZCwgcmV0X3BpZCwgZXhpdF9zdGF0dXM7CiAgICBpbnQgaTsKICAvLyB1c2UgdGhpcyBwYXJ0IHRvIHRlc3QgZXhpdChpbnQgc3RhdHVzKSBhbmQgd2FpdChpbnQqIHN0YXR1cykKIAovLyAgIHByaW50ZigxLCAiXG4gIFBhcnRzIGEgJiBiKSB0ZXN0aW5nIGV4aXQoaW50IHN0YXR1cykgYW5kIHdhaXQoaW50KiBzdGF0dXMpOlxuIik7CgogIGZvciAoaSA9IDA7IGkgPCAyOyBpKyspIHsKICAgIHBpZCA9IGZvcmsoKTsKICAgIGlmIChwaWQgPT0gMCkgeyAvLyBvbmx5IHRoZSBjaGlsZCBleGVjdXRlZCB0aGlzIGNvZGUKICAgICAgaWYgKGkgPT0gMCl7CiAgICAgICAgcHJpbnRmKDEsICIlZCAlZFxuIiwgZ2V0cGlkKCksIDApOwogICAgICAgIGV4aXQoMCk7CiAgICAgIH0KICAgICAgZWxzZXsKCSAgICAgIHByaW50ZigxLCAiJWQgJWRcbiIgLGdldHBpZCgpLCAtMSk7CiAgICAgICAgZXhpdCgtMSk7CiAgICAgIH0gCiAgICB9IGVsc2UgaWYgKHBpZCA+IDApIHsgLy8gb25seSB0aGUgcGFyZW50IGV4ZWN1dGVzIHRoaXMgY29kZQogICAgICByZXRfcGlkID0gd2FpdCgmZXhpdF9zdGF0dXMpOwogICAgICBwcmludGYoMSwgIiVkKyVkXG4iLCByZXRfcGlkLCBleGl0X3N0YXR1cyk7CiAgICB9IGVsc2UgeyAvLyBzb21ldGhpbmcgd2VudCB3cm9uZyB3aXRoIGZvcmsgc3lzdGVtIGNhbGwKCSAgICBwcmludGYoMiwgIlxuRXJyb3IgdXNpbmcgZm9ya1xuIik7CiAgICAgIGV4aXQoLTEpOwogICAgfQogIH0KICByZXR1cm4gMDsKfQoKaW50IHdhaXRQaWQodm9pZCl7CgkKICBpbnQgcmV0X3BpZCwgZXhpdF9zdGF0dXM7CiAgaW50IGk7CiAgaW50IHBpZF9hWzVdPXswLCAwLCAwLCAwLCAwfTsKIC8vIHVzZSB0aGlzIHBhcnQgdG8gdGVzdCB3YWl0KGludCBwaWQsIGludCogc3RhdHVzLCBpbnQgb3B0aW9ucykKCi8vICAgcHJpbnRmKDEsICJcbiAgUGFydCBjKSB0ZXN0aW5nIHdhaXRwaWQoaW50IHBpZCwgaW50KiBzdGF0dXMsIGludCBvcHRpb25zKTpcbiIpOwoKCWZvciAoaSA9IDA7IGkgPDU7IGkrKykgewoJCXBpZF9hW2ldID0gZm9yaygpOwoJCWlmIChwaWRfYVtpXSA9PSAwKSB7IC8vIG9ubHkgdGhlIGNoaWxkIGV4ZWN1dGVkIHRoaXMgY29kZQoJCQlwcmludGYoMSwgIiVkICVkXG4iLCBnZXRwaWQoKSwgZ2V0cGlkKCkgKyA0KTsKCQkJZXhpdChnZXRwaWQoKSArIDQpOwoJCX0KCX0KICBzbGVlcCg1KTsKICBwcmludGYoMSwgIiVkXG4iLHBpZF9hWzNdKTsKICByZXRfcGlkID0gd2FpdHBpZChwaWRfYVszXSwgJmV4aXRfc3RhdHVzLCAwKTsKICBwcmludGYoMSwgIiVkKyVkKyVkXG4iLHJldF9waWQsIGV4aXRfc3RhdHVzLCBwaWRfYVszXSArIDQpOwogIHNsZWVwKDUpOwogIHByaW50ZigxLCAiJWRcbiIscGlkX2FbMV0pOwogIHJldF9waWQgPSB3YWl0cGlkKHBpZF9hWzFdLCAmZXhpdF9zdGF0dXMsIDApOwogIHByaW50ZigxLCAiJWQrJWQrJWRcbiIscmV0X3BpZCwgZXhpdF9zdGF0dXMsIHBpZF9hWzFdICsgNCk7CiAgc2xlZXAoNSk7CiAgcHJpbnRmKDEsICIlZFxuIixwaWRfYVsyXSk7CiAgcmV0X3BpZCA9IHdhaXRwaWQocGlkX2FbMl0sICZleGl0X3N0YXR1cywgMCk7CiAgcHJpbnRmKDEsICIlZCslZCslZFxuIixyZXRfcGlkLCBleGl0X3N0YXR1cywgcGlkX2FbMl0gKyA0KTsKICBzbGVlcCg1KTsKICBwcmludGYoMSwgIiVkXG4iLHBpZF9hWzBdKTsKICByZXRfcGlkID0gd2FpdHBpZChwaWRfYVswXSwgJmV4aXRfc3RhdHVzLCAwKTsKICBwcmludGYoMSwgIiVkKyVkKyVkXG4iLHJldF9waWQsIGV4aXRfc3RhdHVzLCBwaWRfYVswXSArIDQpOwogIHNsZWVwKDUpOwogIHByaW50ZigxLCAiJWRcbiIscGlkX2FbNF0pOwogIHJldF9waWQgPSB3YWl0cGlkKHBpZF9hWzRdLCAmZXhpdF9zdGF0dXMsIDApOwogIHByaW50ZigxLCAiJWQrJWQrJWRcbiIscmV0X3BpZCwgZXhpdF9zdGF0dXMsIHBpZF9hWzRdICsgNCk7CgogIHJldF9waWQgPSB3YWl0cGlkKDk5OTksICZleGl0X3N0YXR1cywgMCk7CiAgcHJpbnRmKDEsICIlZFxuIixyZXRfcGlkKTsKICAvL3ByaW50ZigxLCAiXG4gVGhpcyBpcyB0aGUgcGFyZW50OiBDaGlsZCMgJWQgaGFzIGV4aXRlZCB3aXRoIHN0YXR1cyAlZFxuIixyZXRfcGlkLCBleGl0X3N0YXR1cyk7CgogIHJldF9waWQgPSB3YWl0cGlkKDk5OTksIChpbnQqKSAweGZmZmZmZmZmLCAwKTsKICBwcmludGYoMSwgIiVkXG4iLHJldF9waWQpOwoKICByZXR1cm4gMDsKfQ=="""


from pwn import *
import yaml
import base64
import re

def populate_makefile(filename):
    c = open('Makefile', 'r').read().replace(" -Werror", " ")
    uprogs = re.findall(r'UPROGS=([\w\W]*)fs\.img: mkfs', c)[0].replace("\\\n",'').split()
    uprogs.insert(0, f'_{filename}')
    uprogs = " ".join(uprogs)
    c = re.sub(r'UPROGS=([\w\W]*)fs\.img: mkfs', f'UPROGS={uprogs} \nfs.img: mkfs', c)
    open("Makefile", 'w').write(c)


def run_test(code, program, rubrics, points):
    code = base64.b64decode(code)
    populate_makefile(program)
    with open(program+".c", 'wb') as f:   
        f.write(code)

    p = process("make qemu-nox".split())

    errors = []

    try:
        p.recvuntil(b"init: starting sh\n$", timeout=10)
    except:
        print("[!]Failed to compile and start xv6 with testsuite")
        print("[!]Compile log:", p.recvall().decode('latin-1'))
        print(f"Your score: {points}")
        exit(1)

    rubrics = yaml.safe_load(rubrics)
    full = points

    for rubric in rubrics:
        print(f"[!]Checking [{rubric['name']}]")
        full += rubric["points"]
        try:
            if "cmd" in rubric:
                p.sendline(rubric["cmd"].encode())
            recv = p.recvuntil(rubric["expect"].encode(), timeout=2).decode('latin-1')
            if rubric["expect"] not in recv:
                raise Exception("Wrong output")
            points += rubric["points"]
        except:
            errors.append(rubric["note"])

    if errors:
        print("[!]Errors:")
        for error in errors:
            print("    " + error)
    else:
        print("[!]All check passed!")
    print("=======")
    print(f"Your score: {points} / {full}")

    if errors:
        exit(1)

    p.terminate()
    p.kill()

    return points


point1 = run_test(code1, "lab1_part1", rubrics1, 0)
# point1 = run_test(code1, "lab1_part1", rubrics1, 0)
point23 = run_test(code23, "lab1_part23", rubrics23, point1)
