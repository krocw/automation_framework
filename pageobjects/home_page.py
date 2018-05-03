# _*_ coding=utf-8 _*_
from framework.base_page import BasePage


class HomePage(BasePage):
    textarea = "class_name=>ivu-input"
    begin_btn = "class_name=>ivu-btn"

    def send_textarea(self, text):
        self.type(self.textarea, text)

    def send_begin_btn(self):
        self.click(self.begin_btn)