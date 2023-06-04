/*
 * @Author: yanxiao333 yanxiao_333@126.com
 * @Date: 2023-05-22 20:29:33
 * @LastEditors: yanxiao333 yanxiao_333@126.com
 * @LastEditTime: 2023-05-22 21:08:53
 * @FilePath: \python-js-study-two\520-test\demo123.js
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 */

function v(t) {
    t = replace(/%([0-9A-F]{2})/g, function (n, t) {
        return o(Y1 + t)
    });
    try {
        return z[Q1](t)
    } catch (n) {
        return z[W1][K1](t)[U1](Z1)
    }
}
function h(n, t) {
    t = t || u();
    for (var e = (n = n[$1](_))[R], r = t[R], a = q1, i = H; i < e; i++)
        n[i] = o(n[i][a](H) ^ t[(i + 10) % r][a](H));
    return n[I1](_)
}
var s = 388, z = this
function url(t) {
    // var n;
    // f || F != s || (n = (0,
    //     i[Wt])(m),
    //     s = c[x][k][Pt] = -(0,
    //         i[Wt])(l) || +new z[W] - a2 * n);
    var e, r = +new Date() - (s || H) - 1661224081041, a = [];
    return void 0 === {} && (t[Zt] = {}),

        a = "",
        a = (0,
            v)(a),
        a = (a += v + t[Jt][T](t[Mt], _)) + (v + r) + (v + 3),
        e = (0,
            v)((0,
                h)(a, d))
    return e
}
t = "/account/userinfo"
console.log(url(t))