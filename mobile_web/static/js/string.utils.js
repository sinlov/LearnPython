/**
 *
 * use like
 * <pre>
 *     "http://{0}/{1}".format("www.songyanjun.net", "index.html")
 * </pre>
 * @returns {String}
 */
String.prototype.format = function () {
    if (arguments.length === 0)
        return this;
    for (var s = this, i = 0; i < arguments.length; i++)
        s = s.replace(new RegExp("\\{" + i + "\\}", "g"), arguments[i]);
    return s;
};