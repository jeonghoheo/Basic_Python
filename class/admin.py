# 관리자
"""
관리자는 특별한 사용자다. User 클래스를 상속하는 Admin 클래스를 만들자.
"can add post", "can delete post", "can ban user" 같은 문자열 리스트를
저장하는 privileges 속성을 추가하자. 관리자의 권한을 나열하는 show_privileges()
메서드를 만들자. Admin의 인스턴스를 만들고 메서드를 호출하자.

Privileges 클래스를 따로 만들자. 이 클래스에는 설명한 문자열 리스트를 저장하는
privileges 속성이 있어야 한다. show_privileges() 메서드를 이 클래스로 옮기자.
Privileges의 인스턴스를 Admin 클래스의 속성으로 만들자. 새 Admin 인스턴스를 만들고
메서드를 써서 권한을 출력하자.
"""

class User():
    """User 정보를 요약하고 환영하는 메시지를 만든다"""
    def __init__(self, first_name, last_name,):
        """first_name과 last_name 속성을 초기화한다."""
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        """사용자 정보를 요약해 출력한다"""
        print("\nThis user name is:")
        print(self.first_name.title() + " " + self.last_name.title())

    def greet_user(self):
        """사용자에게 환영 인사를 보낸다."""
        print("\nHello " + self.first_name.title() +
        " " + self.last_name.title())

class Privileges():
    """특권을 저장하고 출력한다."""
    def __init__(self):
        """특권의 속성을 초기화한다."""
        self.privilege = []

    def privileges(self, pri):
        self.privilege.append(pri)

    def show_privileges(self):
        print("\nHere is administer's privileges ")
        for admin_privilege in self.privilege:
            print("- " + admin_privilege.title())

class Admin(User):
    """사용자를 관리하는 관리자"""
    def __init__(self, first_name, last_name):
        """사용자를 속성을 초기화한다."""
        super().__init__(first_name, last_name)
        self.privileges = Privileges()


eric = Admin('eric', 'matthes')
eric.privileges.privileges("can add post")
eric.privileges.privileges("can delete post")
eric.privileges.privileges("can ban user")
eric.describe_user()
eric.privileges.show_privileges()
