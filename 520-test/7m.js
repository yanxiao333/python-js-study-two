/*
 * @Author: yanxiao333 yanxiao_333@126.com
 * @Date: 2023-05-26 21:11:22
 * @LastEditors: yanxiao333 yanxiao_333@126.com
 * @LastEditTime: 2023-05-26 21:18:08
 * @FilePath: \python-js-study-two\520-test\7m.js
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 */

function h(n, t) {
    t = t || u();
    for (var e = (n = n[$1](_))[R], r = t[R], a = q1, i = H; i < e; i++)
        n[i] = o(n[i][a](H) ^ t[(i + 10) % r][a](H));
    return n[I1](_)
}
function v(t) {
    t = z[V1](t)[T](/%([0-9A-F]{2})/g, function (n, t) {
        return o(Y1 + t)
    });
    try {
        return z[Q1](t)
    } catch (n) {
        return z[W1][K1](t)[U1](Z1)
    }
}
function url(t) {
    var e, r = +new Date() - (517 || H) - 1661224081041, a = []
    var d="xyz517cda96abcd"
    e = (0,
        v)((0,
            h)(a, d))
    return e
}

t = "/rank/keywordCoverRank"
console.log(url(t))