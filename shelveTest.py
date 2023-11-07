import shelve, sys, os

class ConstStore :
    STORE_FILE_NAME = "constStore"
    RESTRICTION = "资质限制"
    WORK_METHOD = "工作方法"
    METHOD_NAME = "方法名称"
    SUB_METHOD_NAME = "子方法名称"
    PARENT_ACCOUNT = "上级单位"
    VENDOR_LIST = "供应商名单"
    
    def __init__(self) -> None:
        current_path = os.path.dirname(__file__)
        if not os.path.exists(os.path.join(current_path, self.STORE_FILE_NAME)) :
            self.initDB()
        self.db = shelve.open(self.STORE_FILE_NAME)
    
    def initParentAccount(self) :
        pass
    def initVendorList(self) :
        pass
    def initWorkMethod(self) :
        self.db[""] = [""]
    def initRestriction(self) :
        self.db[self.RESTRICTION] = [
        "安全生产许可证",
        "测绘甲级",
        "测绘乙级",
        "测绘丙级",
        "地质灾害施工甲级",
        "地质灾害施工乙级",
        "地质灾害施工丙级",
        "地质灾害设计甲级",
        "地质灾害设计乙级",
        "地质灾害设计丙级",
        "地质灾害勘查甲级",
        "地质灾害勘查乙级",
        "地质灾害勘查丙级",
        "地质灾害危险性评估甲级",
        "地质灾害危险性评估乙级",
        "地质灾害危险性评估丙级",
        "质量标准体系认证",
        "环境标准体系认证",
        "职业健康标准体系认证",
        "工程勘察综合资质甲级",
        "岩土工程甲级",
        "岩土工程乙级",
        "岩土工程设计甲级",
        "岩土工程设计乙级",
        "岩土工程物探测试检测监测甲级",
        "岩土工程物探测试检测监测乙级",
        "岩土工程勘察甲级",
        "岩土工程勘察乙级",
        "岩土工程勘察丙级",
        "水文地质勘察甲级",
        "水文地质勘察乙级",
        "水文地质勘察丙级",
        "工程测量甲级",
        "工程测量乙级",
        "工程测量丙级",
        ];

    def initDB(self) :
        self.db = shelve.open(self.STORE_FILE_NAME)
        self.initRestriction();
        self.db.close();
    def __del__(self) :
        self.db.close()

    def data(self) :
        return self.db
