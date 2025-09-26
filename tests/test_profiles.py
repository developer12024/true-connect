import pytest

async def test_create_and_get_profile(client):
    payload = {"full_name": "Alice Example", "email": "alice@example.com", "bio": "hello"}
    r = await client.post('/profiles/', json=payload)
    assert r.status_code == 201
    data = r.json()
    assert data['email'] == payload['email']

    pid = data['id']
    r2 = await client.get(f'/profiles/{pid}')
    assert r2.status_code == 200
    assert r2.json()['full_name'] == payload['full_name']

async def test_update_and_delete_profile(client):
    payload = {"full_name": "Bob Example", "email": "bob@example.com"}
    r = await client.post('/profiles/', json=payload)
    assert r.status_code == 201
    pid = r.json()['id']

    r2 = await client.patch(f'/profiles/{pid}', json={"bio": "updated"})
    assert r2.status_code == 200
    assert r2.json()['bio'] == 'updated'

    r3 = await client.delete(f'/profiles/{pid}')
    assert r3.status_code == 204