import httpx
import pytest

@pytest.mark.asyncio
async def test_sign_new_user(default_client: httpx.AsyncClient) -> None:
    payload = {
        "email": "testuser@test.pri",
        "password": "test123",
    }

    # 요청 헤더와 응답을 정의
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    test_response = {
        "message": "가입되었습니다"
    }

    # 요청에 대한 예상 응답 정의
    response = await default_client.post("/user/signup", json=payload, headers=headers)

    # 응답을 비교해서 성공했는지 확인 코드 작성
    assert response.status_code == 200
    assert response.json() == test_response    

# 로그인 라우트 테스트
@pytest.mark.asyncio
async def test_sign_user_in(default_client: httpx.AsyncClient) -> None:
    payload = {
        "username": "testuser@test.pri",
        "password": "test123"
    }

    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    # 예상 응답

    response = await default_client.post("/user/signin", data=payload, headers=headers)

    # 성공 여부

    assert response.status_code == 200
    assert response.json()["token_type"] == "Bearer"