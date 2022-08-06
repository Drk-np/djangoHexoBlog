var searchFunc = function (path, search_id, content_id) {
    var $input = document.getElementById(search_id);
    var $resultContent = document.getElementById(content_id);
    console.log($input.innerHTML);

    function debounce(func, wait, immediate) {
        // result -- 返回值
        let timeout, result;
        let debounced = function () {
            let self = this
            let args = arguments
            clearTimeout(timeout)
            if (immediate) {
                // callNow是立即执行的变量
                let callNow = !timeout
                timeout = setTimeout(() => {
                    timeout = null
                }, wait)
                // 由于最开始timeout为undefined,取反为true,故立即执行
                if (callNow) result = func.apply(self, args)
            } else {
                // 不会立即执行
                timeout = setTimeout(function () {
                    //解决执行函数内部this指向问题以及event指向问题
                    result = func.apply(self, args)
                }, wait)
            }
            return result
        }
        // 取消
        debounced.cancel = function () {
            clearTimeout(timeout)
            timeout = null // 防止内存泄露
        }
        return debounced
    }

    let searchFun = function () {
        if ($input.value.toString().trim() === '') return
        $.ajax({
            url: path,
            dataType: "json",
            data: {
                'title': $input.value.toString().trim()
            },
            success: function (res) {
                // get the contents from search data
                var datas = res.rows
                var str = '<ul class=\"search-result-list\">';
                // var keywords = this.value.trim().toLowerCase().split(/[\s\-]+/);
                $resultContent.innerHTML = "";
                if (datas.length <= 0) {
                    return;
                }
                // perform local searching
                datas.forEach(function (data) {
                    str += "<li><a href='" + 'article/' + data.url + "' class='search-result-title'>" + data.title + "</a>";
                    var content = data.content.trim().replace(/<[^>]+>/g, "");
                    var count = data.content.split($input.value).length - 1
                    // cut out 100 characters
                    var start = count - 20;
                    var end = count + 80;
                    if (start < 0) {
                        start = 0;
                    }
                    if (start == 0) {
                        end = 100;
                    }
                    if (end > content.length) {
                        end = content.length;
                    }
                    var match_content = content.substr(start, end);
                    // highlight all keywords
                    var regS = new RegExp($input.value, "gi");
                    match_content = match_content.replace(regS, "<em class=\"search-keyword\">" + $input.value + "</em>");
                    str += "<p class=\"search-result\">" + match_content + "...</p>"
                    str += "</li>";
                });
                str += "</ul>";
                $resultContent.innerHTML = str;
            }
        })
    }

    $input.addEventListener('input', debounce(searchFun,500,))
}
