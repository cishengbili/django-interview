#coding:utf-8


import requests
import unittest
from urlparse import urljoin

class LeaderBoardTest(unittest.TestCase):

    def setUp(self):
        self.base_url='http://127.0.0.1:8000/'

    def test_push_point(self):

        path = "/push/point"

        # 输入正常情况
        params = {"client_number": "00008", "point": 10000}
        r=requests.get(urljoin(self.base_url, path), params=params)
        result = r.json()
        self.assertEqual(result["success"], True)

        # 缺少参数
        params = {"point": 10000}
        r=requests.get(urljoin(self.base_url, path), params=params)
        result = r.json()
        self.assertEqual(result["success"], False)
        params = {"client_number": "00008"}
        r=requests.get(urljoin(self.base_url, path), params=params)
        result = r.json()
        self.assertEqual(result["success"], False)

        # point 输入非整型数据
        params = {"client_number": "00008", "point": "fffff"}
        r=requests.get(urljoin(self.base_url, path), params=params)
        result = r.json()
        self.assertEqual(result["success"], False)

        # point 输入越限情况
        params = {"client_number": "00008", "point": 100000000}
        r=requests.get(urljoin(self.base_url, path), params=params)
        result = r.json()
        self.assertEqual(result["success"], False)

    def test_get_player_rank(self):

        path = "/player/rank"

        # 输入正常情况
        params = {"client_number": "00008", "rank_start": 3, "rank_end": 7}
        r=requests.get(urljoin(self.base_url, path), params=params)
        result = r.json()
        data = result["data"]
        self.assertEqual(result["success"], True)
        self.assertEqual(data[-1]["client_number"], "00008")

        # 缺少参数
        params = {"client_number": "00008"}
        r=requests.get(urljoin(self.base_url, path), params=params)
        result = r.json()
        self.assertEqual(result["success"], False)

        params = {"rank_start": 3, "rank_end": 7}
        r=requests.get(urljoin(self.base_url, path), params=params)
        result = r.json()
        self.assertEqual(result["success"], False)

        params = {"rank_end": 7}
        r=requests.get(urljoin(self.base_url, path), params=params)
        result = r.json()
        self.assertEqual(result["success"], False)

        # rank 输入非整型数据
        params = {"client_number": "00008", "rank_start": "fdf", "rank_end": 7}
        r=requests.get(urljoin(self.base_url, path), params=params)
        result = r.json()
        self.assertEqual(result["success"], False)

        # rank 输入越界数据
        params = {"client_number": "00008", "rank_start": "3", "rank_end": 100}
        r=requests.get(urljoin(self.base_url, path), params=params)
        result = r.json()
        self.assertEqual(result["success"], True)

        # rank 左侧越界
        params = {"client_number": "00008", "rank_start": "20", "rank_end": 100}
        r=requests.get(urljoin(self.base_url, path), params=params)
        result = r.json()
        data = result["data"]
        self.assertEqual(result["success"], True)
        self.assertEqual(len(data), 1)



if __name__ == "__main__":

    unittest.main()
