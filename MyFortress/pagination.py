def pagination(curent_page, content_list, page_num=5, page_content=10, **kwargs):
    search_param = ''
    for item in kwargs:
        param_item = item+'='+kwargs[item]+'&'
        search_param += param_item
    code_list = []
    curent_page = int(curent_page)
    start_content = (curent_page - 1) * page_content
    end_content = curent_page * page_content
    curent_content = content_list[start_content:end_content]
    content_count = len(content_list)
    p, y = divmod(content_count, page_content)
    if y:
        p = p + 1
    if p < page_num:
        start_page = 1
        end_page = p
    elif curent_page < page_num//2 + 1:
        start_page = 1
        end_page = page_num + 1
    elif curent_page > p - (page_num//2 + 1):
        start_page = p - (page_num - 1)
        end_page = p + 1
    else:
        start_page = curent_page - page_num//2
        end_page = curent_page + (page_num//2 + 1)

    prev_page = curent_page - 1
    next_page = curent_page + 1

    code_list.append('<ul class="pagination">')
    if curent_page == 1:
        code_list.append('<li class="paginate_button page-item previous disabled" id="bootstrap-data-table_previous"><a aria-controls="bootstrap-data-table" data-dt-idx="0" tabindex="0" class="page-link">Previous</a></li>')
    else:
        code_list.append('<li class="paginate_button page-item previous" id="bootstrap-data-table_previous"><a href="/index/?page=%s&%s" aria-controls="bootstrap-data-table" data-dt-idx="0" tabindex="0" class="page-link">Previous</a></li>' % (prev_page, search_param))
    for i in range(start_page, end_page):
        if i == int(curent_page):
            html_code_page = '<li class="paginate_button page-item active"><a href="/index/?page=%s&%s" aria-controls="bootstrap-data-table" data-dt-idx="%s" tabindex="0" class="page-link">%s</a></li>' % (i, search_param, i, i)
        else:
            html_code_page = '<li class="paginate_button page-item"><a href="/index/?page=%s&%s" aria-controls="bootstrap-data-table" data-dt-idx="%s" tabindex="0" class="page-link">%s</a></li>' % (i, search_param, i, i)
        code_list.append(html_code_page)
    if curent_page == p:
        code_list.append('<li class="paginate_button page-item next disabled" id="bootstrap-data-table_next"><a aria-controls="bootstrap-data-table" data-dt-idx="7" tabindex="0" class="page-link">Next</a> </li>')
    else:
        code_list.append('<li class="paginate_button page-item next" id="bootstrap-data-table_next"><a href="/index/?page=%s&%s" aria-controls="bootstrap-data-table" data-dt-idx="7" tabindex="0" class="page-link">Next</a> </li>' % (prev_page, search_param))
    code_list.append('</ul>')
    code_str = ''.join(code_list)
    #return render(request, 'page.html', {'content_list': curent_content, 'code_str': code_str})
    return curent_content, code_str