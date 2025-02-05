import utilities.custom_logger as cl
import logging

class TestStatus():

    log = cl.customLogger(logging.DEBUG)
    resultList = []
    
    def setResults(self, result, message):
        try:
            if result is not None:
                if result:
                    self.log.info("Verification PASS: "  + message)
                    self.resultList.append("PASS")
                    print(self.resultList)
                else:
                    self.log.info("Verification FAIL: "  + message)
                    self.resultList.append("FAIL")
                    print(self.resultList)
            else:
                self.log.error("Verification NONE: "  + message)
                self.resultList.append("FAIL")
                print(self.resultList)
        except:
            self.log.error("Verification EXCEPTION: "  + message)
            self.resultList.append("FAIL")
            print(self.resultList)
        return self.resultList

    def mark(self, result, message):
        """
        Mark the result of a specific step in a test case
        """
        self.setResults(result, message)
    
    def markFinal(self, test_name, result, message):
        """
        Mark the final result of a test case
        """
        self.setResults(result, message)
        if "FAIL" in self.resultList:
            self.log.error(test_name + " FAILED!")
            self.resultList.clear()
            assert True == False
        else:
            self.log.error(test_name + " FAILED!")
            self.resultList.clear()
            assert True == True
