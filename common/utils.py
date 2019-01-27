"""Hệ thống quản lý xử lý back test trên giao dịch chứng khoán
Các thành phần bao gồm:
    - Danh sách các datafeeds: Xử lý lưu trữ các data feed
    - Danh sách các datacenters: Trung tâm dữ liệu
    - Danh sách các strategies: Các chiến lược
    - Danh sách các decision making: Thực hiện việc quyết định realtime
    - Danh sách các traders: thực hiện việc giao dịch

Các plugin giao tiếp với nhau thông qua các setting: 
    SETTINGTYPES: Danh sách các kiểu setting

"""

SETTINGTYPES = (
    ('TEXT','TEXT'),
    ('NUMBER', 'NUMBER'),
    ('DECIMAL', 'DECIMAL'),
    ('COLLECTION_DATA','COLLECTION_DATA'),
)

PLUGINTYPES= (
    ('OTHER','OTHER'),
    ('DATAFEED', 'DATAFEED'),
    ('DATACENTER', 'DATACENTER'),
    ('STRATEGY', 'STRATEGY'),
    ('DECISIONMAKING','DECISIONMAKING'),
    ('TRADER','TRADER'),
)

BACKTESTTYPES = (
    ('START', 'START'),
    ('RESTART', 'RESTART'),
    ('ORDER', 'ORDER'),
    ('INPROCESS', 'INPROCESS'),
    ('COMPLETED', 'COMPLETED'),
)

