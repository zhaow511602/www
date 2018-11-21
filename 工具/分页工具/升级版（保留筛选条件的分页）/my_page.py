class PageInfo(object):
    def __init__(self, current_page, all_count, base_url,page_param_dict,per_page=10, show_page=11):
        """
        :param current_page:
        :param all_count: 数据库总行数
        :param per_page: 每页显示函数
        :return:
        """
        try:
            self.current_page = int(current_page)
        except Exception as e:
            self.current_page = 1
        self.per_page = per_page
        a, b = divmod(all_count, per_page)
        if b:
            a = a + 1
        self.all_pager = a
        self.show_page = show_page
        self.base_url = base_url
        self.page_param_dict = page_param_dict

    @property
    def start(self):
        return (self.current_page - 1) * self.per_page
    @property
    def end(self):
        return self.current_page * self.per_page

    def pager(self):
        # v = "<a href='/custom.html?page=1'>1</a><a href='/custom.html?page=2'>2</a>"
        # return v
        page_list = []
        half = int((self.show_page - 1) / 2)
        # 如果数据总页数 < 11
        if self.all_pager < self.show_page:
            begin = 1
            stop = self.all_pager + 1
        # 如果数据总页数 > 11
        else:
            # 如果当前页 <=5,永远显示1,11
            if self.current_page <= half:
                begin = 1
                stop = self.show_page + 1
            else:
                if self.current_page + half > self.all_pager:
                    begin = self.all_pager - self.show_page + 1
                    stop = self.all_pager + 1
                else:
                    begin = self.current_page - half
                    stop = self.current_page + half + 1
        if self.current_page <= 1:
            prev = "<li><a href='#'>上一页</a></li>"
        else:
            #self.page_param_dict
            #/yg/app01/usergroup/?id=2&name=alex&page=self.current_page - 1
            self.page_param_dict['page'] = self.current_page - 1
            prev = "<li><a href='%s?%s'>上一页</a></li>" % (self.base_url,self.page_param_dict.urlencode() ,)
        page_list.append(prev)
        for i in range(begin, stop):
            self.page_param_dict['page'] = i
            if i == self.current_page:
                temp = "<li class='active'><a  href='%s?%s'>%s</a></li>" % (self.base_url,self.page_param_dict.urlencode(), i,)
            else:
                temp = "<li><a href='%s?%s'>%s</a></li>" % (self.base_url, self.page_param_dict.urlencode(), i,)
            page_list.append(temp)
        if self.current_page >= self.all_pager:
            nex = "<li><a href='#'>下一页</a></li>"
        else:
            self.page_param_dict['page'] = self.current_page + 1
            nex = "<li><a href='%s?%s'>下一页</a></li>" % (self.base_url, self.page_param_dict.urlencode(),)
        page_list.append(nex)
        return ''.join(page_list)
