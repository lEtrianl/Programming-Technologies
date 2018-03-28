def ff(email):
    if email.count('@') == 1:
        st = email.split('@')
        if len(st[0])>0 and len(st[1])>0:
            st = st[1]
            if st.count('.')>0:
                st = st.split('.')
                for i in st:
                    if not i.isalpha():
                        return False
                return True
    return False

print(ff("@.@.@.@."))