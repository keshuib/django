# 封装支付宝工具
# 添加支付宝 SDK
# 在网页服务工具中配置相关信息

"""
注意：
因为目前无法获取支付宝沙箱密钥，
所以 APP_ID、应用私钥、支付宝公钥、网关地址暂时为空。
等获取到沙箱配置后再填写。

具体的工作流程如下
用户点击“立即购买”
        ↓
Django 创建订单
        ↓
调用支付宝 
        ↓
支付宝返回 qr_code
        ↓
后端把 qr_code 返回给前端
        ↓
前端把 qr_code 转成二维码
        ↓
用户用支付宝扫码
        ↓
支付宝完成支付
        ↓
支付宝异步通知 Django
        ↓
Django 验签
        ↓
修改订单状态 = 已支付


"""

# 导入 Python 日志模块
import logging

# 导入 traceback，用于打印完整的异常信息
import traceback

# 导入支付宝客户端配置类
from alipay.aop.api.AlipayClientConfig import AlipayClientConfig

# 导入支付宝默认客户端
from alipay.aop.api.DefaultAlipayClient import DefaultAlipayClient

# 导入当面付预创建订单的数据模型
from alipay.aop.api.domain.AlipayTradePrecreateModel import AlipayTradePrecreateModel

# 导入当面付预创建请求类
from alipay.aop.api.request.AlipayTradePrecreateRequest import AlipayTradePrecreateRequest

# 导入当面付预创建响应类
from alipay.aop.api.response.AlipayTradePrecreateResponse import AlipayTradePrecreateResponse


# =========================
# 配置日志
# =========================

# 配置日志的基本信息
logging.basicConfig(
    # 设置日志级别为 INFO
    level=logging.INFO,

    # 设置日志输出格式
    # %(asctime)s：时间
    # %(levelname)s：日志级别
    # %(message)s：日志内容
    format='%(asctime)s %(levelname)s %(message)s',

    # 使用追加模式写入日志
    filemode='a'
)

# 获取当前模块的日志对象
logger = logging.getLogger(__name__)


# =========================
# 支付宝配置
# =========================

# 支付宝服务器地址
# 也就是支付宝 API 的网关地址
# 当前没有沙箱配置，所以暂时为空
ALIPAY_SERVER_URL = ""

# 支付宝应用 ID
# 这里填写你在支付宝开放平台创建应用后获得的 APP_ID
# 例如你的 APP_ID 如果是 jiaoyu_env，就写：
# ALIPAY_APP_ID = "jiaoyu_env"
ALIPAY_APP_ID = ""

# 开发者应用私钥
# 用于对发送给支付宝的请求进行签名
# 当前没有沙箱私钥，所以暂时为空
ALIPAY_APP_PRIVATE_KEY = ""

# 支付宝公钥
# 用于验证支付宝返回的数据
# 当前没有沙箱支付宝公钥，所以暂时为空
ALIPAY_PUBLIC_KEY = ""


# =========================
# 创建支付宝客户端
# =========================

def get_alipay_client():

    # 创建支付宝客户端配置对象
    alipay_client_config = AlipayClientConfig()

    # 设置支付宝服务器地址
    # 告诉 SDK 请求发送到哪个支付宝服务器
    alipay_client_config.server_url = ALIPAY_SERVER_URL

    # 设置支付宝应用 ID
    # 用来标识当前调用支付宝接口的是哪个应用
    alipay_client_config.app_id = ALIPAY_APP_ID

    # 设置开发者应用私钥
    # SDK 会使用这个私钥对请求进行签名
    alipay_client_config.app_private_key = ALIPAY_APP_PRIVATE_KEY

    # 设置支付宝公钥
    # 用于验证支付宝返回的数据
    alipay_client_config.alipay_public_key = ALIPAY_PUBLIC_KEY


    # 配置通知支付成功回调地址 内网穿透生成的临时域名+回调接口地址
    request.notify_url=""

    # 根据上面的配置创建支付宝客户端
    client = DefaultAlipayClient(
        alipay_client_config,
        logger
    )

    # 返回支付宝客户端对象
    return client


# =========================
# 测试支付宝当面付
# =========================

# 判断当前文件是不是直接运行
# 如果是直接运行，才执行下面的测试代码
if __name__ == '__main__':

    # 获取支付宝客户端
    client = get_alipay_client()

    # =========================
    # 构造订单信息
    # =========================

    # 创建当面付预创建订单模型
    # 用来保存需要发送给支付宝的订单信息
    model = AlipayTradePrecreateModel()

    # 设置商户订单号
    # 这个订单号由我们自己的 Django 项目生成
    # 实际项目中不能一直写死
    model.out_trade_no = "20150320010101001"

    # 设置订单支付金额
    # 支付金额使用字符串形式
    model.total_amount = "88.88"

    # 设置订单商品名称
    # 例如教育平台中可以写成：
    # "Python Django 全栈课程"
    model.subject = "Iphone6 16G"


    # =========================
    # 创建请求
    # =========================

    # 创建支付宝当面付预创建请求对象
    # biz_model=model 表示把刚才的订单信息传给支付宝
    request = AlipayTradePrecreateRequest(
        biz_model=model
    )


    # =========================
    # 执行 API 调用
    # =========================

    # 用来保存支付宝返回的结果
    # 初始值设置为 False
    response_content = False

    try:

        # 调用支付宝客户端执行请求
        # request 中包含了订单信息
        # 这里会真正向支付宝服务器发送请求
        response_content = client.execute(request)

    except Exception:

        # 如果请求过程中出现异常
        # 打印完整的异常信息
        print(traceback.format_exc())


    # =========================
    # 判断请求是否成功
    # =========================

    # 如果没有获取到支付宝返回的数据
    if not response_content:

        # 表示 API 调用失败
        print("failed execute")

    else:

        # 创建支付宝预创建响应对象
        # 用于解析支付宝返回的数据
        response = AlipayTradePrecreateResponse()

        # 解析支付宝返回的原始数据
        # 将返回的数据转换成 response 对象中的属性
        response.parse_response_content(
            response_content
        )


        # =========================
        # 请求成功
        # =========================

        # 判断支付宝业务是否执行成功
        if response.is_success():

            # 输出请求成功
            print("支付宝请求成功")

            # 获取支付宝生成的交易号
            # trade_no 是支付宝自己的交易编号
            print(
                "trade_no:",
                response.trade_no
            )

            # 获取支付宝返回的二维码内容
            # 后面可以交给前端二维码组件生成二维码
            print(
                "qr_code:",
                response.qr_code
            )


        # =========================
        # 请求失败
        # =========================

        else:

            # 输出支付宝返回的错误信息
            #
            # response.code：
            # 支付宝错误码
            #
            # response.msg：
            # 错误信息
            #
            # response.sub_code：
            # 具体业务错误码
            #
            # response.sub_msg：
            # 具体业务错误信息
            print(
                response.code,
                response.msg,
                response.sub_code,
                response.sub_msg
            )