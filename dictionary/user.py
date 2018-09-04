# 딕셔너리에 루프 실행하기
user_0 = {
    'username' : 'efermi',
    'first' : 'enrico',
    'last' : 'fermi',
}

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)
"""
딕셔너리에 for 루프를 실행할 때는 각 키-값 쌍의 키와 값을 저장할 변수 이름을 정한다
이들 변수 이름은 원하는 대로 써도 된다. 이 코드는 변수 약어에도 똑같이 동작한다
다만, 'key'라고 쓸 것을 'k'라고 쓰면서 절약하는 시간보다 나중에 이 코드를 보면서
'k?' k가 뭐지? 하고 생각하는 시간이 더 길 수 있으므로, 지나치게 약어를 많이 쓰는
습관은 좋지 않다
for 문에서 딕셔너리 이름다음에 있는 item() 메서드는 키-값 쌍 리스트를 반환한다
그러면 for 루프는 이들 각 쌍을 제공된 두 변수에 저장한다
"""
