(function(){'use strict';var m;function ba(a){var b=0;return function(){return b<a.length?{done:!1,value:a[b++]}:{done:!0}}}
var ca="function"==typeof Object.defineProperties?Object.defineProperty:function(a,b,c){if(a==Array.prototype||a==Object.prototype)return a;a[b]=c.value;return a};
function da(a){a=["object"==typeof globalThis&&globalThis,a,"object"==typeof window&&window,"object"==typeof self&&self,"object"==typeof global&&global];for(var b=0;b<a.length;++b){var c=a[b];if(c&&c.Math==Math)return c}throw Error("Cannot find global object");}
var ha=da(this);function u(a,b){if(b)a:{var c=ha;a=a.split(".");for(var d=0;d<a.length-1;d++){var e=a[d];if(!(e in c))break a;c=c[e]}a=a[a.length-1];d=c[a];b=b(d);b!=d&&null!=b&&ca(c,a,{configurable:!0,writable:!0,value:b})}}
u("Symbol",function(a){function b(f){if(this instanceof b)throw new TypeError("Symbol is not a constructor");return new c(d+(f||"")+"_"+e++,f)}
function c(f,g){this.h=f;ca(this,"description",{configurable:!0,writable:!0,value:g})}
if(a)return a;c.prototype.toString=function(){return this.h};
var d="jscomp_symbol_"+(1E9*Math.random()>>>0)+"_",e=0;return b});
u("Symbol.iterator",function(a){if(a)return a;a=Symbol("Symbol.iterator");for(var b="Array Int8Array Uint8Array Uint8ClampedArray Int16Array Uint16Array Int32Array Uint32Array Float32Array Float64Array".split(" "),c=0;c<b.length;c++){var d=ha[b[c]];"function"===typeof d&&"function"!=typeof d.prototype[a]&&ca(d.prototype,a,{configurable:!0,writable:!0,value:function(){return ja(ba(this))}})}return a});
function ja(a){a={next:a};a[Symbol.iterator]=function(){return this};
return a}
function ka(a){return a.raw=a}
function na(a,b){a.raw=b;return a}
function v(a){var b="undefined"!=typeof Symbol&&Symbol.iterator&&a[Symbol.iterator];if(b)return b.call(a);if("number"==typeof a.length)return{next:ba(a)};throw Error(String(a)+" is not an iterable or ArrayLike");}
function oa(a){if(!(a instanceof Array)){a=v(a);for(var b,c=[];!(b=a.next()).done;)c.push(b.value);a=c}return a}
function pa(a,b){return Object.prototype.hasOwnProperty.call(a,b)}
var qa="function"==typeof Object.assign?Object.assign:function(a,b){for(var c=1;c<arguments.length;c++){var d=arguments[c];if(d)for(var e in d)pa(d,e)&&(a[e]=d[e])}return a};
u("Object.assign",function(a){return a||qa});
var ra="function"==typeof Object.create?Object.create:function(a){function b(){}
b.prototype=a;return new b},sa=function(){function a(){function c(){}
new c;Reflect.construct(c,[],function(){});
return new c instanceof c}
if("undefined"!=typeof Reflect&&Reflect.construct){if(a())return Reflect.construct;var b=Reflect.construct;return function(c,d,e){c=b(c,d);e&&Reflect.setPrototypeOf(c,e.prototype);return c}}return function(c,d,e){void 0===e&&(e=c);
e=ra(e.prototype||Object.prototype);return Function.prototype.apply.call(c,e,d)||e}}(),ta;
if("function"==typeof Object.setPrototypeOf)ta=Object.setPrototypeOf;else{var ua;a:{var va={a:!0},wa={};try{wa.__proto__=va;ua=wa.a;break a}catch(a){}ua=!1}ta=ua?function(a,b){a.__proto__=b;if(a.__proto__!==b)throw new TypeError(a+" is not extensible");return a}:null}var xa=ta;
function w(a,b){a.prototype=ra(b.prototype);a.prototype.constructor=a;if(xa)xa(a,b);else for(var c in b)if("prototype"!=c)if(Object.defineProperties){var d=Object.getOwnPropertyDescriptor(b,c);d&&Object.defineProperty(a,c,d)}else a[c]=b[c];a.Aa=b.prototype}
function ya(){this.A=!1;this.v=null;this.i=void 0;this.h=1;this.m=this.l=0;this.S=this.j=null}
function za(a){if(a.A)throw new TypeError("Generator is already running");a.A=!0}
ya.prototype.D=function(a){this.i=a};
function Aa(a,b){a.j={exception:b,nd:!0};a.h=a.l||a.m}
ya.prototype.return=function(a){this.j={return:a};this.h=this.m};
ya.prototype.yield=function(a,b){this.h=b;return{value:a}};
ya.prototype.B=function(a){this.h=a};
function Ba(a,b,c){a.l=b;void 0!=c&&(a.m=c)}
function Ca(a){a.l=0;var b=a.j.exception;a.j=null;return b}
function Ea(a){var b=a.S.splice(0)[0];(b=a.j=a.j||b)?b.nd?a.h=a.l||a.m:void 0!=b.B&&a.m<b.B?(a.h=b.B,a.j=null):a.h=a.m:a.h=0}
function Fa(a){this.h=new ya;this.i=a}
function Ga(a,b){za(a.h);var c=a.h.v;if(c)return Ha(a,"return"in c?c["return"]:function(d){return{value:d,done:!0}},b,a.h.return);
a.h.return(b);return Ia(a)}
function Ha(a,b,c,d){try{var e=b.call(a.h.v,c);if(!(e instanceof Object))throw new TypeError("Iterator result "+e+" is not an object");if(!e.done)return a.h.A=!1,e;var f=e.value}catch(g){return a.h.v=null,Aa(a.h,g),Ia(a)}a.h.v=null;d.call(a.h,f);return Ia(a)}
function Ia(a){for(;a.h.h;)try{var b=a.i(a.h);if(b)return a.h.A=!1,{value:b.value,done:!1}}catch(c){a.h.i=void 0,Aa(a.h,c)}a.h.A=!1;if(a.h.j){b=a.h.j;a.h.j=null;if(b.nd)throw b.exception;return{value:b.return,done:!0}}return{value:void 0,done:!0}}
function Ja(a){this.next=function(b){za(a.h);a.h.v?b=Ha(a,a.h.v.next,b,a.h.D):(a.h.D(b),b=Ia(a));return b};
this.throw=function(b){za(a.h);a.h.v?b=Ha(a,a.h.v["throw"],b,a.h.D):(Aa(a.h,b),b=Ia(a));return b};
this.return=function(b){return Ga(a,b)};
this[Symbol.iterator]=function(){return this}}
function Ka(a){function b(d){return a.next(d)}
function c(d){return a.throw(d)}
return new Promise(function(d,e){function f(g){g.done?d(g.value):Promise.resolve(g.value).then(b,c).then(f,e)}
f(a.next())})}
function A(a){return Ka(new Ja(new Fa(a)))}
function B(){for(var a=Number(this),b=[],c=a;c<arguments.length;c++)b[c-a]=arguments[c];return b}
u("Reflect",function(a){return a?a:{}});
u("Reflect.construct",function(){return sa});
u("Reflect.setPrototypeOf",function(a){return a?a:xa?function(b,c){try{return xa(b,c),!0}catch(d){return!1}}:null});
u("Promise",function(a){function b(g){this.h=0;this.j=void 0;this.i=[];this.A=!1;var h=this.l();try{g(h.resolve,h.reject)}catch(k){h.reject(k)}}
function c(){this.h=null}
function d(g){return g instanceof b?g:new b(function(h){h(g)})}
if(a)return a;c.prototype.i=function(g){if(null==this.h){this.h=[];var h=this;this.j(function(){h.v()})}this.h.push(g)};
var e=ha.setTimeout;c.prototype.j=function(g){e(g,0)};
c.prototype.v=function(){for(;this.h&&this.h.length;){var g=this.h;this.h=[];for(var h=0;h<g.length;++h){var k=g[h];g[h]=null;try{k()}catch(l){this.l(l)}}}this.h=null};
c.prototype.l=function(g){this.j(function(){throw g;})};
b.prototype.l=function(){function g(l){return function(n){k||(k=!0,l.call(h,n))}}
var h=this,k=!1;return{resolve:g(this.ba),reject:g(this.v)}};
b.prototype.ba=function(g){if(g===this)this.v(new TypeError("A Promise cannot resolve to itself"));else if(g instanceof b)this.ha(g);else{a:switch(typeof g){case "object":var h=null!=g;break a;case "function":h=!0;break a;default:h=!1}h?this.Y(g):this.m(g)}};
b.prototype.Y=function(g){var h=void 0;try{h=g.then}catch(k){this.v(k);return}"function"==typeof h?this.ta(h,g):this.m(g)};
b.prototype.v=function(g){this.D(2,g)};
b.prototype.m=function(g){this.D(1,g)};
b.prototype.D=function(g,h){if(0!=this.h)throw Error("Cannot settle("+g+", "+h+"): Promise already settled in state"+this.h);this.h=g;this.j=h;2===this.h&&this.ea();this.S()};
b.prototype.ea=function(){var g=this;e(function(){if(g.V()){var h=ha.console;"undefined"!==typeof h&&h.error(g.j)}},1)};
b.prototype.V=function(){if(this.A)return!1;var g=ha.CustomEvent,h=ha.Event,k=ha.dispatchEvent;if("undefined"===typeof k)return!0;"function"===typeof g?g=new g("unhandledrejection",{cancelable:!0}):"function"===typeof h?g=new h("unhandledrejection",{cancelable:!0}):(g=ha.document.createEvent("CustomEvent"),g.initCustomEvent("unhandledrejection",!1,!0,g));g.promise=this;g.reason=this.j;return k(g)};
b.prototype.S=function(){if(null!=this.i){for(var g=0;g<this.i.length;++g)f.i(this.i[g]);this.i=null}};
var f=new c;b.prototype.ha=function(g){var h=this.l();g.Wb(h.resolve,h.reject)};
b.prototype.ta=function(g,h){var k=this.l();try{g.call(h,k.resolve,k.reject)}catch(l){k.reject(l)}};
b.prototype.then=function(g,h){function k(r,t){return"function"==typeof r?function(x){try{l(r(x))}catch(z){n(z)}}:t}
var l,n,p=new b(function(r,t){l=r;n=t});
this.Wb(k(g,l),k(h,n));return p};
b.prototype.catch=function(g){return this.then(void 0,g)};
b.prototype.Wb=function(g,h){function k(){switch(l.h){case 1:g(l.j);break;case 2:h(l.j);break;default:throw Error("Unexpected state: "+l.h);}}
var l=this;null==this.i?f.i(k):this.i.push(k);this.A=!0};
b.resolve=d;b.reject=function(g){return new b(function(h,k){k(g)})};
b.race=function(g){return new b(function(h,k){for(var l=v(g),n=l.next();!n.done;n=l.next())d(n.value).Wb(h,k)})};
b.all=function(g){var h=v(g),k=h.next();return k.done?d([]):new b(function(l,n){function p(x){return function(z){r[x]=z;t--;0==t&&l(r)}}
var r=[],t=0;do r.push(void 0),t++,d(k.value).Wb(p(r.length-1),n),k=h.next();while(!k.done)})};
return b});
u("WeakMap",function(a){function b(k){this.h=(h+=Math.random()+1).toString();if(k){k=v(k);for(var l;!(l=k.next()).done;)l=l.value,this.set(l[0],l[1])}}
function c(){}
function d(k){var l=typeof k;return"object"===l&&null!==k||"function"===l}
function e(k){if(!pa(k,g)){var l=new c;ca(k,g,{value:l})}}
function f(k){var l=Object[k];l&&(Object[k]=function(n){if(n instanceof c)return n;Object.isExtensible(n)&&e(n);return l(n)})}
if(function(){if(!a||!Object.seal)return!1;try{var k=Object.seal({}),l=Object.seal({}),n=new a([[k,2],[l,3]]);if(2!=n.get(k)||3!=n.get(l))return!1;n.delete(k);n.set(l,4);return!n.has(k)&&4==n.get(l)}catch(p){return!1}}())return a;
var g="$jscomp_hidden_"+Math.random();f("freeze");f("preventExtensions");f("seal");var h=0;b.prototype.set=function(k,l){if(!d(k))throw Error("Invalid WeakMap key");e(k);if(!pa(k,g))throw Error("WeakMap key fail: "+k);k[g][this.h]=l;return this};
b.prototype.get=function(k){return d(k)&&pa(k,g)?k[g][this.h]:void 0};
b.prototype.has=function(k){return d(k)&&pa(k,g)&&pa(k[g],this.h)};
b.prototype.delete=function(k){return d(k)&&pa(k,g)&&pa(k[g],this.h)?delete k[g][this.h]:!1};
return b});
u("Map",function(a){function b(){var h={};return h.previous=h.next=h.head=h}
function c(h,k){var l=h[1];return ja(function(){if(l){for(;l.head!=h[1];)l=l.previous;for(;l.next!=l.head;)return l=l.next,{done:!1,value:k(l)};l=null}return{done:!0,value:void 0}})}
function d(h,k){var l=k&&typeof k;"object"==l||"function"==l?f.has(k)?l=f.get(k):(l=""+ ++g,f.set(k,l)):l="p_"+k;var n=h[0][l];if(n&&pa(h[0],l))for(h=0;h<n.length;h++){var p=n[h];if(k!==k&&p.key!==p.key||k===p.key)return{id:l,list:n,index:h,entry:p}}return{id:l,list:n,index:-1,entry:void 0}}
function e(h){this[0]={};this[1]=b();this.size=0;if(h){h=v(h);for(var k;!(k=h.next()).done;)k=k.value,this.set(k[0],k[1])}}
if(function(){if(!a||"function"!=typeof a||!a.prototype.entries||"function"!=typeof Object.seal)return!1;try{var h=Object.seal({x:4}),k=new a(v([[h,"s"]]));if("s"!=k.get(h)||1!=k.size||k.get({x:4})||k.set({x:4},"t")!=k||2!=k.size)return!1;var l=k.entries(),n=l.next();if(n.done||n.value[0]!=h||"s"!=n.value[1])return!1;n=l.next();return n.done||4!=n.value[0].x||"t"!=n.value[1]||!l.next().done?!1:!0}catch(p){return!1}}())return a;
var f=new WeakMap;e.prototype.set=function(h,k){h=0===h?0:h;var l=d(this,h);l.list||(l.list=this[0][l.id]=[]);l.entry?l.entry.value=k:(l.entry={next:this[1],previous:this[1].previous,head:this[1],key:h,value:k},l.list.push(l.entry),this[1].previous.next=l.entry,this[1].previous=l.entry,this.size++);return this};
e.prototype.delete=function(h){h=d(this,h);return h.entry&&h.list?(h.list.splice(h.index,1),h.list.length||delete this[0][h.id],h.entry.previous.next=h.entry.next,h.entry.next.previous=h.entry.previous,h.entry.head=null,this.size--,!0):!1};
e.prototype.clear=function(){this[0]={};this[1]=this[1].previous=b();this.size=0};
e.prototype.has=function(h){return!!d(this,h).entry};
e.prototype.get=function(h){return(h=d(this,h).entry)&&h.value};
e.prototype.entries=function(){return c(this,function(h){return[h.key,h.value]})};
e.prototype.keys=function(){return c(this,function(h){return h.key})};
e.prototype.values=function(){return c(this,function(h){return h.value})};
e.prototype.forEach=function(h,k){for(var l=this.entries(),n;!(n=l.next()).done;)n=n.value,h.call(k,n[1],n[0],this)};
e.prototype[Symbol.iterator]=e.prototype.entries;var g=0;return e});
function La(a,b,c){if(null==a)throw new TypeError("The 'this' value for String.prototype."+c+" must not be null or undefined");if(b instanceof RegExp)throw new TypeError("First argument to String.prototype."+c+" must not be a regular expression");return a+""}
u("String.prototype.endsWith",function(a){return a?a:function(b,c){var d=La(this,b,"endsWith");b+="";void 0===c&&(c=d.length);c=Math.max(0,Math.min(c|0,d.length));for(var e=b.length;0<e&&0<c;)if(d[--c]!=b[--e])return!1;return 0>=e}});
u("Object.setPrototypeOf",function(a){return a||xa});
u("Array.prototype.find",function(a){return a?a:function(b,c){a:{var d=this;d instanceof String&&(d=String(d));for(var e=d.length,f=0;f<e;f++){var g=d[f];if(b.call(c,g,f,d)){b=g;break a}}b=void 0}return b}});
u("String.prototype.startsWith",function(a){return a?a:function(b,c){var d=La(this,b,"startsWith");b+="";var e=d.length,f=b.length;c=Math.max(0,Math.min(c|0,d.length));for(var g=0;g<f&&c<e;)if(d[c++]!=b[g++])return!1;return g>=f}});
u("Number.isFinite",function(a){return a?a:function(b){return"number"!==typeof b?!1:!isNaN(b)&&Infinity!==b&&-Infinity!==b}});
function Ma(a,b){a instanceof String&&(a+="");var c=0,d=!1,e={next:function(){if(!d&&c<a.length){var f=c++;return{value:b(f,a[f]),done:!1}}d=!0;return{done:!0,value:void 0}}};
e[Symbol.iterator]=function(){return e};
return e}
u("Array.prototype.keys",function(a){return a?a:function(){return Ma(this,function(b){return b})}});
u("Set",function(a){function b(c){this.h=new Map;if(c){c=v(c);for(var d;!(d=c.next()).done;)this.add(d.value)}this.size=this.h.size}
if(function(){if(!a||"function"!=typeof a||!a.prototype.entries||"function"!=typeof Object.seal)return!1;try{var c=Object.seal({x:4}),d=new a(v([c]));if(!d.has(c)||1!=d.size||d.add(c)!=d||1!=d.size||d.add({x:4})!=d||2!=d.size)return!1;var e=d.entries(),f=e.next();if(f.done||f.value[0]!=c||f.value[1]!=c)return!1;f=e.next();return f.done||f.value[0]==c||4!=f.value[0].x||f.value[1]!=f.value[0]?!1:e.next().done}catch(g){return!1}}())return a;
b.prototype.add=function(c){c=0===c?0:c;this.h.set(c,c);this.size=this.h.size;return this};
b.prototype.delete=function(c){c=this.h.delete(c);this.size=this.h.size;return c};
b.prototype.clear=function(){this.h.clear();this.size=0};
b.prototype.has=function(c){return this.h.has(c)};
b.prototype.entries=function(){return this.h.entries()};
b.prototype.values=function(){return this.h.values()};
b.prototype.keys=b.prototype.values;b.prototype[Symbol.iterator]=b.prototype.values;b.prototype.forEach=function(c,d){var e=this;this.h.forEach(function(f){return c.call(d,f,f,e)})};
return b});
u("Array.prototype.values",function(a){return a?a:function(){return Ma(this,function(b,c){return c})}});
u("Object.values",function(a){return a?a:function(b){var c=[],d;for(d in b)pa(b,d)&&c.push(b[d]);return c}});
u("Object.is",function(a){return a?a:function(b,c){return b===c?0!==b||1/b===1/c:b!==b&&c!==c}});
u("Array.prototype.includes",function(a){return a?a:function(b,c){var d=this;d instanceof String&&(d=String(d));var e=d.length;c=c||0;for(0>c&&(c=Math.max(c+e,0));c<e;c++){var f=d[c];if(f===b||Object.is(f,b))return!0}return!1}});
u("String.prototype.includes",function(a){return a?a:function(b,c){return-1!==La(this,b,"includes").indexOf(b,c||0)}});
u("Number.MAX_SAFE_INTEGER",function(){return 9007199254740991});
u("Number.isInteger",function(a){return a?a:function(b){return Number.isFinite(b)?b===Math.floor(b):!1}});
u("Number.isSafeInteger",function(a){return a?a:function(b){return Number.isInteger(b)&&Math.abs(b)<=Number.MAX_SAFE_INTEGER}});
u("Math.trunc",function(a){return a?a:function(b){b=Number(b);if(isNaN(b)||Infinity===b||-Infinity===b||0===b)return b;var c=Math.floor(Math.abs(b));return 0>b?-c:c}});
u("Array.prototype.entries",function(a){return a?a:function(){return Ma(this,function(b,c){return[b,c]})}});
u("Array.from",function(a){return a?a:function(b,c,d){c=null!=c?c:function(h){return h};
var e=[],f="undefined"!=typeof Symbol&&Symbol.iterator&&b[Symbol.iterator];if("function"==typeof f){b=f.call(b);for(var g=0;!(f=b.next()).done;)e.push(c.call(d,f.value,g++))}else for(f=b.length,g=0;g<f;g++)e.push(c.call(d,b[g],g));return e}});
u("Number.isNaN",function(a){return a?a:function(b){return"number"===typeof b&&isNaN(b)}});
u("Object.entries",function(a){return a?a:function(b){var c=[],d;for(d in b)pa(b,d)&&c.push([d,b[d]]);return c}});
u("globalThis",function(a){return a||ha});/*

 Copyright The Closure Library Authors.
 SPDX-License-Identifier: Apache-2.0
*/
var Na=Na||{},C=this||self;function D(a,b,c){a=a.split(".");c=c||C;a[0]in c||"undefined"==typeof c.execScript||c.execScript("var "+a[0]);for(var d;a.length&&(d=a.shift());)a.length||void 0===b?c[d]&&c[d]!==Object.prototype[d]?c=c[d]:c=c[d]={}:c[d]=b}
function Oa(a){var b=E("CLOSURE_FLAGS");a=b&&b[a];return null!=a?a:!1}
function E(a,b){a=a.split(".");b=b||C;for(var c=0;c<a.length;c++)if(b=b[a[c]],null==b)return null;return b}
function Pa(a){var b=typeof a;return"object"!=b?b:a?Array.isArray(a)?"array":b:"null"}
function Qa(a){var b=Pa(a);return"array"==b||"object"==b&&"number"==typeof a.length}
function Ra(a){var b=typeof a;return"object"==b&&null!=a||"function"==b}
function Sa(a){return Object.prototype.hasOwnProperty.call(a,Ta)&&a[Ta]||(a[Ta]=++Ua)}
var Ta="closure_uid_"+(1E9*Math.random()>>>0),Ua=0;function Va(a,b,c){return a.call.apply(a.bind,arguments)}
function Wa(a,b,c){if(!a)throw Error();if(2<arguments.length){var d=Array.prototype.slice.call(arguments,2);return function(){var e=Array.prototype.slice.call(arguments);Array.prototype.unshift.apply(e,d);return a.apply(b,e)}}return function(){return a.apply(b,arguments)}}
function Xa(a,b,c){Xa=Function.prototype.bind&&-1!=Function.prototype.bind.toString().indexOf("native code")?Va:Wa;return Xa.apply(null,arguments)}
function Ya(a,b){var c=Array.prototype.slice.call(arguments,1);return function(){var d=c.slice();d.push.apply(d,arguments);return a.apply(this,d)}}
function Za(){return Date.now()}
function $a(a,b){function c(){}
c.prototype=b.prototype;a.Aa=b.prototype;a.prototype=new c;a.prototype.constructor=a;a.base=function(d,e,f){for(var g=Array(arguments.length-2),h=2;h<arguments.length;h++)g[h-2]=arguments[h];return b.prototype[e].apply(d,g)}}
function ab(a){return a}
;function bb(a,b){if(Error.captureStackTrace)Error.captureStackTrace(this,bb);else{var c=Error().stack;c&&(this.stack=c)}a&&(this.message=String(a));void 0!==b&&(this.cause=b)}
$a(bb,Error);bb.prototype.name="CustomError";function cb(a){a=a.url;var b=/[?&]dsh=1(&|$)/.test(a);this.j=!b&&/[?&]ae=1(&|$)/.test(a);this.l=!b&&/[?&]ae=2(&|$)/.test(a);if((this.h=/[?&]adurl=([^&]*)/.exec(a))&&this.h[1]){try{var c=decodeURIComponent(this.h[1])}catch(d){c=null}this.i=c}}
;function db(){}
function eb(a){var b=!1,c;return function(){b||(c=a(),b=!0);return c}}
;var fb=Array.prototype.indexOf?function(a,b){return Array.prototype.indexOf.call(a,b,void 0)}:function(a,b){if("string"===typeof a)return"string"!==typeof b||1!=b.length?-1:a.indexOf(b,0);
for(var c=0;c<a.length;c++)if(c in a&&a[c]===b)return c;return-1},gb=Array.prototype.forEach?function(a,b,c){Array.prototype.forEach.call(a,b,c)}:function(a,b,c){for(var d=a.length,e="string"===typeof a?a.split(""):a,f=0;f<d;f++)f in e&&b.call(c,e[f],f,a)},hb=Array.prototype.filter?function(a,b){return Array.prototype.filter.call(a,b,void 0)}:function(a,b){for(var c=a.length,d=[],e=0,f="string"===typeof a?a.split(""):a,g=0;g<c;g++)if(g in f){var h=f[g];
b.call(void 0,h,g,a)&&(d[e++]=h)}return d},ib=Array.prototype.map?function(a,b){return Array.prototype.map.call(a,b,void 0)}:function(a,b){for(var c=a.length,d=Array(c),e="string"===typeof a?a.split(""):a,f=0;f<c;f++)f in e&&(d[f]=b.call(void 0,e[f],f,a));
return d},jb=Array.prototype.reduce?function(a,b,c){return Array.prototype.reduce.call(a,b,c)}:function(a,b,c){var d=c;
gb(a,function(e,f){d=b.call(void 0,d,e,f,a)});
return d};
function kb(a,b){a:{for(var c=a.length,d="string"===typeof a?a.split(""):a,e=0;e<c;e++)if(e in d&&b.call(void 0,d[e],e,a)){b=e;break a}b=-1}return 0>b?null:"string"===typeof a?a.charAt(b):a[b]}
function lb(a,b){b=fb(a,b);var c;(c=0<=b)&&Array.prototype.splice.call(a,b,1);return c}
function mb(a,b){for(var c=1;c<arguments.length;c++){var d=arguments[c];if(Qa(d)){var e=a.length||0,f=d.length||0;a.length=e+f;for(var g=0;g<f;g++)a[e+g]=d[g]}else a.push(d)}}
;function nb(a,b){for(var c in a)b.call(void 0,a[c],c,a)}
function ob(a){var b=pb,c;for(c in b)if(a.call(void 0,b[c],c,b))return c}
function qb(a){for(var b in a)return!1;return!0}
function rb(a,b){if(null!==a&&b in a)throw Error('The object already contains the key "'+b+'"');a[b]=!0}
function sb(a){return null!==a&&"privembed"in a?a.privembed:!1}
function tb(a,b){for(var c in a)if(!(c in b)||a[c]!==b[c])return!1;for(var d in b)if(!(d in a))return!1;return!0}
function ub(a){var b={},c;for(c in a)b[c]=a[c];return b}
function vb(a){if(!a||"object"!==typeof a)return a;if("function"===typeof a.clone)return a.clone();if("undefined"!==typeof Map&&a instanceof Map)return new Map(a);if("undefined"!==typeof Set&&a instanceof Set)return new Set(a);if(a instanceof Date)return new Date(a.getTime());var b=Array.isArray(a)?[]:"function"!==typeof ArrayBuffer||"function"!==typeof ArrayBuffer.isView||!ArrayBuffer.isView(a)||a instanceof DataView?{}:new a.constructor(a.length),c;for(c in a)b[c]=vb(a[c]);return b}
var wb="constructor hasOwnProperty isPrototypeOf propertyIsEnumerable toLocaleString toString valueOf".split(" ");function xb(a,b){for(var c,d,e=1;e<arguments.length;e++){d=arguments[e];for(c in d)a[c]=d[c];for(var f=0;f<wb.length;f++)c=wb[f],Object.prototype.hasOwnProperty.call(d,c)&&(a[c]=d[c])}}
;var yb;function zb(){if(void 0===yb){var a=null,b=C.trustedTypes;if(b&&b.createPolicy){try{a=b.createPolicy("goog#html",{createHTML:ab,createScript:ab,createScriptURL:ab})}catch(c){C.console&&C.console.error(c.message)}yb=a}else yb=a}return yb}
;function Ab(a,b){this.h=a===Bb&&b||""}
Ab.prototype.toString=function(){return this.h};
function Cb(a){return new Ab(Bb,a)}
var Bb={};Cb("");function Db(a){this.h=a}
Db.prototype.toString=function(){return this.h+""};
function Eb(a){if(a instanceof Db&&a.constructor===Db)return a.h;Pa(a);return"type_error:TrustedResourceUrl"}
var Fb={};function Gb(a){var b=zb();a=b?b.createScriptURL(a):a;return new Db(a,Fb)}
;function Hb(a){this.h=a}
Hb.prototype.toString=function(){return this.h.toString()};
var Ib={};var Jb=String.prototype.trim?function(a){return a.trim()}:function(a){return/^[\s\xa0]*([\s\S]*?)[\s\xa0]*$/.exec(a)[1]};var Kb=Oa(610401301),Lb=Oa(188588736);function Mb(){var a=C.navigator;return a&&(a=a.userAgent)?a:""}
var Nb,Ob=C.navigator;Nb=Ob?Ob.userAgentData||null:null;function Pb(a){return Kb?Nb?Nb.brands.some(function(b){return(b=b.brand)&&-1!=b.indexOf(a)}):!1:!1}
function F(a){return-1!=Mb().indexOf(a)}
;function Qb(){return Kb?!!Nb&&0<Nb.brands.length:!1}
function Rb(){return Qb()?!1:F("Opera")}
function Sb(){return Qb()?!1:F("Trident")||F("MSIE")}
function Tb(){return F("Firefox")||F("FxiOS")}
function Ub(){return Qb()?Pb("Chromium"):(F("Chrome")||F("CriOS"))&&!(Qb()?0:F("Edge"))||F("Silk")}
;function Vb(a){this.h=a}
Vb.prototype.toString=function(){return this.h.toString()};/*

 SPDX-License-Identifier: Apache-2.0
*/
var Wb={};function Xb(){}
Xb.prototype.toString=function(){return this.ud.toString()};var Yb=new Hb("about:invalid#zClosurez",Ib);function Zb(a){for(var b=0,c=0;c<a.length;++c)b=31*b+a.charCodeAt(c)>>>0;return b}
;var $b=RegExp("^(?:([^:/?#.]+):)?(?://(?:([^\\\\/?#]*)@)?([^\\\\/?#]*?)(?::([0-9]+))?(?=[\\\\/?#]|$))?([^?#]+)?(?:\\?([^#]*))?(?:#([\\s\\S]*))?$");function ac(a){return a?decodeURI(a):a}
function bc(a,b){return b.match($b)[a]||null}
function cc(a){return ac(bc(3,a))}
function dc(a){var b=a.match($b);a=b[5];var c=b[6];b=b[7];var d="";a&&(d+=a);c&&(d+="?"+c);b&&(d+="#"+b);return d}
function ec(a){var b=a.indexOf("#");return 0>b?a:a.slice(0,b)}
function fc(a,b,c){if(Array.isArray(b))for(var d=0;d<b.length;d++)fc(a,String(b[d]),c);else null!=b&&c.push(a+(""===b?"":"="+encodeURIComponent(String(b))))}
function hc(a){var b=[],c;for(c in a)fc(c,a[c],b);return b.join("&")}
function ic(a,b){b=hc(b);if(b){var c=a.indexOf("#");0>c&&(c=a.length);var d=a.indexOf("?");if(0>d||d>c){d=c;var e=""}else e=a.substring(d+1,c);a=[a.slice(0,d),e,a.slice(c)];c=a[1];a[1]=b?c?c+"&"+b:b:c;b=a[0]+(a[1]?"?"+a[1]:"")+a[2]}else b=a;return b}
function jc(a,b,c,d){for(var e=c.length;0<=(b=a.indexOf(c,b))&&b<d;){var f=a.charCodeAt(b-1);if(38==f||63==f)if(f=a.charCodeAt(b+e),!f||61==f||38==f||35==f)return b;b+=e+1}return-1}
var kc=/#|$/,lc=/[?&]($|#)/;function mc(a,b){for(var c=a.search(kc),d=0,e,f=[];0<=(e=jc(a,d,b,c));)f.push(a.substring(d,e)),d=Math.min(a.indexOf("&",e)+1||c,c);f.push(a.slice(d));return f.join("").replace(lc,"$1")}
;function nc(a){this.h=a}
;function oc(a,b,c){this.l=a;this.j=b;this.fields=c||[];this.h=new Map}
m=oc.prototype;m.Pd=function(a){var b=B.apply(1,arguments),c=this.xc(b);c?c.push(new nc(a)):this.Cd(a,b)};
m.Cd=function(a){var b=this.Vc(B.apply(1,arguments));this.h.set(b,[new nc(a)])};
m.xc=function(){var a=this.Vc(B.apply(0,arguments));return this.h.has(a)?this.h.get(a):void 0};
m.he=function(){var a=this.xc(B.apply(0,arguments));return a&&a.length?a[0]:void 0};
m.clear=function(){this.h.clear()};
m.Vc=function(){var a=B.apply(0,arguments);return a?a.join(","):"key"};function pc(a,b){oc.call(this,a,3,b)}
w(pc,oc);pc.prototype.i=function(a){var b=B.apply(1,arguments),c=0,d=this.he(b);d&&(c=d.h);this.Cd(c+a,b)};function qc(a,b){oc.call(this,a,2,b)}
w(qc,oc);qc.prototype.record=function(a){this.Pd(a,B.apply(1,arguments))};function rc(a){a&&"function"==typeof a.dispose&&a.dispose()}
;function sc(a){for(var b=0,c=arguments.length;b<c;++b){var d=arguments[b];Qa(d)?sc.apply(null,d):rc(d)}}
;function H(){this.ob=this.ob;this.v=this.v}
m=H.prototype;m.ob=!1;m.Z=function(){return this.ob};
m.dispose=function(){this.ob||(this.ob=!0,this.R())};
function tc(a,b){a.addOnDisposeCallback(Ya(rc,b))}
m.addOnDisposeCallback=function(a,b){this.ob?void 0!==b?a.call(b):a():(this.v||(this.v=[]),this.v.push(void 0!==b?Xa(a,b):a))};
m.R=function(){if(this.v)for(;this.v.length;)this.v.shift()()};function uc(a,b){this.type=a;this.h=this.target=b;this.defaultPrevented=this.j=!1}
uc.prototype.stopPropagation=function(){this.j=!0};
uc.prototype.preventDefault=function(){this.defaultPrevented=!0};function vc(a){var b=E("window.location.href");null==a&&(a='Unknown Error of type "null/undefined"');if("string"===typeof a)return{message:a,name:"Unknown error",lineNumber:"Not available",fileName:b,stack:"Not available"};var c=!1;try{var d=a.lineNumber||a.line||"Not available"}catch(g){d="Not available",c=!0}try{var e=a.fileName||a.filename||a.sourceURL||C.$googDebugFname||b}catch(g){e="Not available",c=!0}b=wc(a);if(!(!c&&a.lineNumber&&a.fileName&&a.stack&&a.message&&a.name)){c=a.message;if(null==
c){if(a.constructor&&a.constructor instanceof Function){if(a.constructor.name)c=a.constructor.name;else if(c=a.constructor,xc[c])c=xc[c];else{c=String(c);if(!xc[c]){var f=/function\s+([^\(]+)/m.exec(c);xc[c]=f?f[1]:"[Anonymous]"}c=xc[c]}c='Unknown Error of type "'+c+'"'}else c="Unknown Error of unknown type";"function"===typeof a.toString&&Object.prototype.toString!==a.toString&&(c+=": "+a.toString())}return{message:c,name:a.name||"UnknownError",lineNumber:d,fileName:e,stack:b||"Not available"}}return{message:a.message,
name:a.name,lineNumber:a.lineNumber,fileName:a.fileName,stack:b}}
function wc(a,b){b||(b={});b[yc(a)]=!0;var c=a.stack||"";(a=a.cause)&&!b[yc(a)]&&(c+="\nCaused by: ",a.stack&&0==a.stack.indexOf(a.toString())||(c+="string"===typeof a?a:a.message+"\n"),c+=wc(a,b));return c}
function yc(a){var b="";"function"===typeof a.toString&&(b=""+a);return b+a.stack}
var xc={};var zc=function(){if(!C.addEventListener||!Object.defineProperty)return!1;var a=!1,b=Object.defineProperty({},"passive",{get:function(){a=!0}});
try{var c=function(){};
C.addEventListener("test",c,b);C.removeEventListener("test",c,b)}catch(d){}return a}();function Ac(){return Kb?!!Nb&&!!Nb.platform:!1}
function Bc(){return F("iPhone")&&!F("iPod")&&!F("iPad")}
;function Cc(a){Cc[" "](a);return a}
Cc[" "]=function(){};var Dc=Rb(),Ec=Sb(),Fc=F("Edge"),Gc=F("Gecko")&&!(-1!=Mb().toLowerCase().indexOf("webkit")&&!F("Edge"))&&!(F("Trident")||F("MSIE"))&&!F("Edge"),Hc=-1!=Mb().toLowerCase().indexOf("webkit")&&!F("Edge");Hc&&F("Mobile");Ac()||F("Macintosh");Ac()||F("Windows");(Ac()?"Linux"===Nb.platform:F("Linux"))||Ac()||F("CrOS");var Ic=Ac()?"Android"===Nb.platform:F("Android");Bc();F("iPad");F("iPod");Bc()||F("iPad")||F("iPod");Mb().toLowerCase().indexOf("kaios");
function Jc(){var a=C.document;return a?a.documentMode:void 0}
var Kc;a:{var Lc="",Mc=function(){var a=Mb();if(Gc)return/rv:([^\);]+)(\)|;)/.exec(a);if(Fc)return/Edge\/([\d\.]+)/.exec(a);if(Ec)return/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(a);if(Hc)return/WebKit\/(\S+)/.exec(a);if(Dc)return/(?:Version)[ \/]?(\S+)/.exec(a)}();
Mc&&(Lc=Mc?Mc[1]:"");if(Ec){var Nc=Jc();if(null!=Nc&&Nc>parseFloat(Lc)){Kc=String(Nc);break a}}Kc=Lc}var Oc=Kc,Pc;if(C.document&&Ec){var Qc=Jc();Pc=Qc?Qc:parseInt(Oc,10)||void 0}else Pc=void 0;var Rc=Pc;function Sc(a,b){uc.call(this,a?a.type:"");this.relatedTarget=this.h=this.target=null;this.button=this.screenY=this.screenX=this.clientY=this.clientX=0;this.key="";this.charCode=this.keyCode=0;this.metaKey=this.shiftKey=this.altKey=this.ctrlKey=!1;this.state=null;this.pointerId=0;this.pointerType="";this.i=null;a&&this.init(a,b)}
$a(Sc,uc);var Tc={2:"touch",3:"pen",4:"mouse"};
Sc.prototype.init=function(a,b){var c=this.type=a.type,d=a.changedTouches&&a.changedTouches.length?a.changedTouches[0]:null;this.target=a.target||a.srcElement;this.h=b;if(b=a.relatedTarget){if(Gc){a:{try{Cc(b.nodeName);var e=!0;break a}catch(f){}e=!1}e||(b=null)}}else"mouseover"==c?b=a.fromElement:"mouseout"==c&&(b=a.toElement);this.relatedTarget=b;d?(this.clientX=void 0!==d.clientX?d.clientX:d.pageX,this.clientY=void 0!==d.clientY?d.clientY:d.pageY,this.screenX=d.screenX||0,this.screenY=d.screenY||
0):(this.clientX=void 0!==a.clientX?a.clientX:a.pageX,this.clientY=void 0!==a.clientY?a.clientY:a.pageY,this.screenX=a.screenX||0,this.screenY=a.screenY||0);this.button=a.button;this.keyCode=a.keyCode||0;this.key=a.key||"";this.charCode=a.charCode||("keypress"==c?a.keyCode:0);this.ctrlKey=a.ctrlKey;this.altKey=a.altKey;this.shiftKey=a.shiftKey;this.metaKey=a.metaKey;this.pointerId=a.pointerId||0;this.pointerType="string"===typeof a.pointerType?a.pointerType:Tc[a.pointerType]||"";this.state=a.state;
this.i=a;a.defaultPrevented&&Sc.Aa.preventDefault.call(this)};
Sc.prototype.stopPropagation=function(){Sc.Aa.stopPropagation.call(this);this.i.stopPropagation?this.i.stopPropagation():this.i.cancelBubble=!0};
Sc.prototype.preventDefault=function(){Sc.Aa.preventDefault.call(this);var a=this.i;a.preventDefault?a.preventDefault():a.returnValue=!1};var Uc="closure_listenable_"+(1E6*Math.random()|0);var Vc=0;function Wc(a,b,c,d,e){this.listener=a;this.proxy=null;this.src=b;this.type=c;this.capture=!!d;this.ac=e;this.key=++Vc;this.Mb=this.Vb=!1}
function Xc(a){a.Mb=!0;a.listener=null;a.proxy=null;a.src=null;a.ac=null}
;function Yc(a){this.src=a;this.listeners={};this.h=0}
Yc.prototype.add=function(a,b,c,d,e){var f=a.toString();a=this.listeners[f];a||(a=this.listeners[f]=[],this.h++);var g=Zc(a,b,d,e);-1<g?(b=a[g],c||(b.Vb=!1)):(b=new Wc(b,this.src,f,!!d,e),b.Vb=c,a.push(b));return b};
Yc.prototype.remove=function(a,b,c,d){a=a.toString();if(!(a in this.listeners))return!1;var e=this.listeners[a];b=Zc(e,b,c,d);return-1<b?(Xc(e[b]),Array.prototype.splice.call(e,b,1),0==e.length&&(delete this.listeners[a],this.h--),!0):!1};
function $c(a,b){var c=b.type;c in a.listeners&&lb(a.listeners[c],b)&&(Xc(b),0==a.listeners[c].length&&(delete a.listeners[c],a.h--))}
function Zc(a,b,c,d){for(var e=0;e<a.length;++e){var f=a[e];if(!f.Mb&&f.listener==b&&f.capture==!!c&&f.ac==d)return e}return-1}
;var ad="closure_lm_"+(1E6*Math.random()|0),bd={},cd=0;function dd(a,b,c,d,e){if(d&&d.once)ed(a,b,c,d,e);else if(Array.isArray(b))for(var f=0;f<b.length;f++)dd(a,b[f],c,d,e);else c=fd(c),a&&a[Uc]?a.listen(b,c,Ra(d)?!!d.capture:!!d,e):gd(a,b,c,!1,d,e)}
function gd(a,b,c,d,e,f){if(!b)throw Error("Invalid event type");var g=Ra(e)?!!e.capture:!!e,h=hd(a);h||(a[ad]=h=new Yc(a));c=h.add(b,c,d,g,f);if(!c.proxy){d=id();c.proxy=d;d.src=a;d.listener=c;if(a.addEventListener)zc||(e=g),void 0===e&&(e=!1),a.addEventListener(b.toString(),d,e);else if(a.attachEvent)a.attachEvent(jd(b.toString()),d);else if(a.addListener&&a.removeListener)a.addListener(d);else throw Error("addEventListener and attachEvent are unavailable.");cd++}}
function id(){function a(c){return b.call(a.src,a.listener,c)}
var b=kd;return a}
function ed(a,b,c,d,e){if(Array.isArray(b))for(var f=0;f<b.length;f++)ed(a,b[f],c,d,e);else c=fd(c),a&&a[Uc]?a.h.add(String(b),c,!0,Ra(d)?!!d.capture:!!d,e):gd(a,b,c,!0,d,e)}
function ld(a,b,c,d,e){if(Array.isArray(b))for(var f=0;f<b.length;f++)ld(a,b[f],c,d,e);else(d=Ra(d)?!!d.capture:!!d,c=fd(c),a&&a[Uc])?a.h.remove(String(b),c,d,e):a&&(a=hd(a))&&(b=a.listeners[b.toString()],a=-1,b&&(a=Zc(b,c,d,e)),(c=-1<a?b[a]:null)&&md(c))}
function md(a){if("number"!==typeof a&&a&&!a.Mb){var b=a.src;if(b&&b[Uc])$c(b.h,a);else{var c=a.type,d=a.proxy;b.removeEventListener?b.removeEventListener(c,d,a.capture):b.detachEvent?b.detachEvent(jd(c),d):b.addListener&&b.removeListener&&b.removeListener(d);cd--;(c=hd(b))?($c(c,a),0==c.h&&(c.src=null,b[ad]=null)):Xc(a)}}}
function jd(a){return a in bd?bd[a]:bd[a]="on"+a}
function kd(a,b){if(a.Mb)a=!0;else{b=new Sc(b,this);var c=a.listener,d=a.ac||a.src;a.Vb&&md(a);a=c.call(d,b)}return a}
function hd(a){a=a[ad];return a instanceof Yc?a:null}
var nd="__closure_events_fn_"+(1E9*Math.random()>>>0);function fd(a){if("function"===typeof a)return a;a[nd]||(a[nd]=function(b){return a.handleEvent(b)});
return a[nd]}
;function od(){H.call(this);this.h=new Yc(this);this.Za=this;this.ha=null}
$a(od,H);od.prototype[Uc]=!0;m=od.prototype;m.addEventListener=function(a,b,c,d){dd(this,a,b,c,d)};
m.removeEventListener=function(a,b,c,d){ld(this,a,b,c,d)};
function pd(a,b){var c=a.ha;if(c){var d=[];for(var e=1;c;c=c.ha)d.push(c),++e}a=a.Za;c=b.type||b;"string"===typeof b?b=new uc(b,a):b instanceof uc?b.target=b.target||a:(e=b,b=new uc(c,a),xb(b,e));e=!0;if(d)for(var f=d.length-1;!b.j&&0<=f;f--){var g=b.h=d[f];e=qd(g,c,!0,b)&&e}b.j||(g=b.h=a,e=qd(g,c,!0,b)&&e,b.j||(e=qd(g,c,!1,b)&&e));if(d)for(f=0;!b.j&&f<d.length;f++)g=b.h=d[f],e=qd(g,c,!1,b)&&e}
m.R=function(){od.Aa.R.call(this);this.removeAllListeners();this.ha=null};
m.listen=function(a,b,c,d){return this.h.add(String(a),b,!1,c,d)};
m.removeAllListeners=function(a){if(this.h){var b=this.h;a=a&&a.toString();var c=0,d;for(d in b.listeners)if(!a||d==a){for(var e=b.listeners[d],f=0;f<e.length;f++)++c,Xc(e[f]);delete b.listeners[d];b.h--}b=c}else b=0;return b};
function qd(a,b,c,d){b=a.h.listeners[String(b)];if(!b)return!0;b=b.concat();for(var e=!0,f=0;f<b.length;++f){var g=b[f];if(g&&!g.Mb&&g.capture==c){var h=g.listener,k=g.ac||g.src;g.Vb&&$c(a.h,g);e=!1!==h.call(k,d)&&e}}return e&&!d.defaultPrevented}
;function rd(a,b){this.j=a;this.l=b;this.i=0;this.h=null}
rd.prototype.get=function(){if(0<this.i){this.i--;var a=this.h;this.h=a.next;a.next=null}else a=this.j();return a};
function sd(a,b){a.l(b);100>a.i&&(a.i++,b.next=a.h,a.h=b)}
;function td(a,b){this.x=void 0!==a?a:0;this.y=void 0!==b?b:0}
m=td.prototype;m.clone=function(){return new td(this.x,this.y)};
m.equals=function(a){return a instanceof td&&(this==a?!0:this&&a?this.x==a.x&&this.y==a.y:!1)};
m.ceil=function(){this.x=Math.ceil(this.x);this.y=Math.ceil(this.y);return this};
m.floor=function(){this.x=Math.floor(this.x);this.y=Math.floor(this.y);return this};
m.round=function(){this.x=Math.round(this.x);this.y=Math.round(this.y);return this};
m.scale=function(a,b){this.x*=a;this.y*="number"===typeof b?b:a;return this};function ud(a,b){this.width=a;this.height=b}
m=ud.prototype;m.clone=function(){return new ud(this.width,this.height)};
m.aspectRatio=function(){return this.width/this.height};
m.ceil=function(){this.width=Math.ceil(this.width);this.height=Math.ceil(this.height);return this};
m.floor=function(){this.width=Math.floor(this.width);this.height=Math.floor(this.height);return this};
m.round=function(){this.width=Math.round(this.width);this.height=Math.round(this.height);return this};
m.scale=function(a,b){this.width*=a;this.height*="number"===typeof b?b:a;return this};function vd(a){var b=document;return"string"===typeof a?b.getElementById(a):a}
function wd(a){var b=document;a=String(a);"application/xhtml+xml"===b.contentType&&(a=a.toLowerCase());return b.createElement(a)}
function xd(a,b){for(var c=0;a;){if(b(a))return a;a=a.parentNode;c++}return null}
;var yd;function zd(){var a=C.MessageChannel;"undefined"===typeof a&&"undefined"!==typeof window&&window.postMessage&&window.addEventListener&&!F("Presto")&&(a=function(){var e=wd("IFRAME");e.style.display="none";document.documentElement.appendChild(e);var f=e.contentWindow;e=f.document;e.open();e.close();var g="callImmediate"+Math.random(),h="file:"==f.location.protocol?"*":f.location.protocol+"//"+f.location.host;e=Xa(function(k){if(("*"==h||k.origin==h)&&k.data==g)this.port1.onmessage()},this);
f.addEventListener("message",e,!1);this.port1={};this.port2={postMessage:function(){f.postMessage(g,h)}}});
if("undefined"!==typeof a&&!Sb()){var b=new a,c={},d=c;b.port1.onmessage=function(){if(void 0!==c.next){c=c.next;var e=c.bd;c.bd=null;e()}};
return function(e){d.next={bd:e};d=d.next;b.port2.postMessage(0)}}return function(e){C.setTimeout(e,0)}}
;function Ad(a){C.setTimeout(function(){throw a;},0)}
;function Bd(){this.i=this.h=null}
Bd.prototype.add=function(a,b){var c=Cd.get();c.set(a,b);this.i?this.i.next=c:this.h=c;this.i=c};
Bd.prototype.remove=function(){var a=null;this.h&&(a=this.h,this.h=this.h.next,this.h||(this.i=null),a.next=null);return a};
var Cd=new rd(function(){return new Dd},function(a){return a.reset()});
function Dd(){this.next=this.scope=this.h=null}
Dd.prototype.set=function(a,b){this.h=a;this.scope=b;this.next=null};
Dd.prototype.reset=function(){this.next=this.scope=this.h=null};var Ed,Fd=!1,Gd=new Bd;function Hd(a,b){Ed||Id();Fd||(Ed(),Fd=!0);Gd.add(a,b)}
function Id(){if(C.Promise&&C.Promise.resolve){var a=C.Promise.resolve(void 0);Ed=function(){a.then(Jd)}}else Ed=function(){var b=Jd;
"function"!==typeof C.setImmediate||C.Window&&C.Window.prototype&&(Qb()||!F("Edge"))&&C.Window.prototype.setImmediate==C.setImmediate?(yd||(yd=zd()),yd(b)):C.setImmediate(b)}}
function Jd(){for(var a;a=Gd.remove();){try{a.h.call(a.scope)}catch(b){Ad(b)}sd(Cd,a)}Fd=!1}
;function Kd(a){this.h=0;this.A=void 0;this.l=this.i=this.j=null;this.v=this.m=!1;if(a!=db)try{var b=this;a.call(void 0,function(c){Ld(b,2,c)},function(c){Ld(b,3,c)})}catch(c){Ld(this,3,c)}}
function Md(){this.next=this.context=this.h=this.i=this.child=null;this.j=!1}
Md.prototype.reset=function(){this.context=this.h=this.i=this.child=null;this.j=!1};
var Nd=new rd(function(){return new Md},function(a){a.reset()});
function Od(a,b,c){var d=Nd.get();d.i=a;d.h=b;d.context=c;return d}
function Pd(a){return new Kd(function(b,c){c(a)})}
Kd.prototype.then=function(a,b,c){return Qd(this,"function"===typeof a?a:null,"function"===typeof b?b:null,c)};
Kd.prototype.$goog_Thenable=!0;m=Kd.prototype;m.nc=function(a,b){return Qd(this,null,a,b)};
m.catch=Kd.prototype.nc;m.cancel=function(a){if(0==this.h){var b=new Rd(a);Hd(function(){Sd(this,b)},this)}};
function Sd(a,b){if(0==a.h)if(a.j){var c=a.j;if(c.i){for(var d=0,e=null,f=null,g=c.i;g&&(g.j||(d++,g.child==a&&(e=g),!(e&&1<d)));g=g.next)e||(f=g);e&&(0==c.h&&1==d?Sd(c,b):(f?(d=f,d.next==c.l&&(c.l=d),d.next=d.next.next):Td(c),Ud(c,e,3,b)))}a.j=null}else Ld(a,3,b)}
function Vd(a,b){a.i||2!=a.h&&3!=a.h||Wd(a);a.l?a.l.next=b:a.i=b;a.l=b}
function Qd(a,b,c,d){var e=Od(null,null,null);e.child=new Kd(function(f,g){e.i=b?function(h){try{var k=b.call(d,h);f(k)}catch(l){g(l)}}:f;
e.h=c?function(h){try{var k=c.call(d,h);void 0===k&&h instanceof Rd?g(h):f(k)}catch(l){g(l)}}:g});
e.child.j=a;Vd(a,e);return e.child}
m.hf=function(a){this.h=0;Ld(this,2,a)};
m.jf=function(a){this.h=0;Ld(this,3,a)};
function Ld(a,b,c){if(0==a.h){a===c&&(b=3,c=new TypeError("Promise cannot resolve to itself"));a.h=1;a:{var d=c,e=a.hf,f=a.jf;if(d instanceof Kd){Vd(d,Od(e||db,f||null,a));var g=!0}else{if(d)try{var h=!!d.$goog_Thenable}catch(l){h=!1}else h=!1;if(h)d.then(e,f,a),g=!0;else{if(Ra(d))try{var k=d.then;if("function"===typeof k){Xd(d,k,e,f,a);g=!0;break a}}catch(l){f.call(a,l);g=!0;break a}g=!1}}}g||(a.A=c,a.h=b,a.j=null,Wd(a),3!=b||c instanceof Rd||Yd(a,c))}}
function Xd(a,b,c,d,e){function f(k){h||(h=!0,d.call(e,k))}
function g(k){h||(h=!0,c.call(e,k))}
var h=!1;try{b.call(a,g,f)}catch(k){f(k)}}
function Wd(a){a.m||(a.m=!0,Hd(a.ae,a))}
function Td(a){var b=null;a.i&&(b=a.i,a.i=b.next,b.next=null);a.i||(a.l=null);return b}
m.ae=function(){for(var a;a=Td(this);)Ud(this,a,this.h,this.A);this.m=!1};
function Ud(a,b,c,d){if(3==c&&b.h&&!b.j)for(;a&&a.v;a=a.j)a.v=!1;if(b.child)b.child.j=null,Zd(b,c,d);else try{b.j?b.i.call(b.context):Zd(b,c,d)}catch(e){$d.call(null,e)}sd(Nd,b)}
function Zd(a,b,c){2==b?a.i.call(a.context,c):a.h&&a.h.call(a.context,c)}
function Yd(a,b){a.v=!0;Hd(function(){a.v&&$d.call(null,b)})}
var $d=Ad;function Rd(a){bb.call(this,a)}
$a(Rd,bb);Rd.prototype.name="cancel";function ae(a,b){od.call(this);this.j=a||1;this.i=b||C;this.l=Xa(this.ff,this);this.m=Za()}
$a(ae,od);m=ae.prototype;m.enabled=!1;m.Ea=null;m.setInterval=function(a){this.j=a;this.Ea&&this.enabled?(this.stop(),this.start()):this.Ea&&this.stop()};
m.ff=function(){if(this.enabled){var a=Za()-this.m;0<a&&a<.8*this.j?this.Ea=this.i.setTimeout(this.l,this.j-a):(this.Ea&&(this.i.clearTimeout(this.Ea),this.Ea=null),pd(this,"tick"),this.enabled&&(this.stop(),this.start()))}};
m.start=function(){this.enabled=!0;this.Ea||(this.Ea=this.i.setTimeout(this.l,this.j),this.m=Za())};
m.stop=function(){this.enabled=!1;this.Ea&&(this.i.clearTimeout(this.Ea),this.Ea=null)};
m.R=function(){ae.Aa.R.call(this);this.stop();delete this.i};
function be(a,b,c){if("function"===typeof a)c&&(a=Xa(a,c));else if(a&&"function"==typeof a.handleEvent)a=Xa(a.handleEvent,a);else throw Error("Invalid listener argument");return 2147483647<Number(b)?-1:C.setTimeout(a,b||0)}
;function ce(a){H.call(this);this.D=a;this.j=0;this.l=100;this.m=!1;this.i=new Map;this.A=new Set;this.flushInterval=3E4;this.h=new ae(this.flushInterval);this.h.listen("tick",this.Oa,!1,this);tc(this,this.h)}
w(ce,H);m=ce.prototype;m.sendIsolatedPayload=function(a){this.m=a;this.l=1};
function de(a){a.h.enabled||a.h.start();a.j++;a.j>=a.l&&a.Oa()}
m.Oa=function(){var a=this.i.values();a=[].concat(oa(a)).filter(function(b){return b.h.size});
a.length&&this.D.flush(a,this.m);ee(a);this.j=0;this.h.enabled&&this.h.stop()};
m.Rb=function(a){var b=B.apply(1,arguments);this.i.has(a)||this.i.set(a,new pc(a,b))};
m.sc=function(a){var b=B.apply(1,arguments);this.i.has(a)||this.i.set(a,new qc(a,b))};
function fe(a,b){return a.A.has(b)?void 0:a.i.get(b)}
m.oc=function(a){this.Od(a,1,B.apply(1,arguments))};
m.Od=function(a,b){var c=B.apply(2,arguments),d=fe(this,a);d&&d instanceof pc&&(d.i(b,c),de(this))};
m.record=function(a,b){var c=B.apply(2,arguments),d=fe(this,a);d&&d instanceof qc&&(d.record(b,c),de(this))};
function ee(a){for(var b=0;b<a.length;b++)a[b].clear()}
;function ge(a){this.h=a;this.h.Rb("/client_streamz/bg/fic",{oa:3,na:"ke"})}
function he(a){this.h=a;this.h.Rb("/client_streamz/bg/fiec",{oa:3,na:"rk"},{oa:3,na:"ke"},{oa:2,na:"ec"},{oa:3,na:"em"})}
function ie(a){this.h=a;this.h.sc("/client_streamz/bg/fil",{oa:3,na:"rk"},{oa:3,na:"ke"})}
ie.prototype.record=function(a,b,c){this.h.record("/client_streamz/bg/fil",a,b,c)};
function je(a){this.h=a;this.h.Rb("/client_streamz/bg/fcc",{oa:2,na:"ph"},{oa:3,na:"ke"})}
function ke(a){this.h=a;this.h.sc("/client_streamz/bg/fcd",{oa:2,na:"ph"},{oa:3,na:"ke"})}
ke.prototype.record=function(a,b,c){this.h.record("/client_streamz/bg/fcd",a,b,c)};
function le(a){this.h=a;this.h.Rb("/client_streamz/bg/fsc",{oa:3,na:"rk"},{oa:3,na:"ke"})}
function me(a){this.h=a;this.h.sc("/client_streamz/bg/fsl",{oa:3,na:"rk"},{oa:3,na:"ke"})}
me.prototype.record=function(a,b,c){this.h.record("/client_streamz/bg/fsl",a,b,c)};var ne={toString:function(a){var b=[],c=0;a-=-2147483648;b[c++]="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".charAt(a%52);for(a=Math.floor(a/52);0<a;)b[c++]="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789".charAt(a%62),a=Math.floor(a/62);return b.join("")}};function oe(a){function b(){c-=d;c-=e;c^=e>>>13;d-=e;d-=c;d^=c<<8;e-=c;e-=d;e^=d>>>13;c-=d;c-=e;c^=e>>>12;d-=e;d-=c;d^=c<<16;e-=c;e-=d;e^=d>>>5;c-=d;c-=e;c^=e>>>3;d-=e;d-=c;d^=c<<10;e-=c;e-=d;e^=d>>>15}
a=pe(a);for(var c=2654435769,d=2654435769,e=314159265,f=a.length,g=f,h=0;12<=g;g-=12,h+=12)c+=qe(a,h),d+=qe(a,h+4),e+=qe(a,h+8),b();e+=f;switch(g){case 11:e+=a[h+10]<<24;case 10:e+=a[h+9]<<16;case 9:e+=a[h+8]<<8;case 8:d+=a[h+7]<<24;case 7:d+=a[h+6]<<16;case 6:d+=a[h+5]<<8;case 5:d+=a[h+4];case 4:c+=a[h+3]<<24;case 3:c+=a[h+2]<<16;case 2:c+=a[h+1]<<8;case 1:c+=a[h+0]}b();return ne.toString(e)}
function pe(a){for(var b=[],c=0;c<a.length;c++)b.push(a.charCodeAt(c));return b}
function qe(a,b){return a[b+0]+(a[b+1]<<8)+(a[b+2]<<16)+(a[b+3]<<24)}
;Tb();var re=Bc()||F("iPod"),se=F("iPad");!F("Android")||Ub()||Tb()||Rb()||F("Silk");Ub();var te=F("Safari")&&!(Ub()||(Qb()?0:F("Coast"))||Rb()||(Qb()?0:F("Edge"))||(Qb()?Pb("Microsoft Edge"):F("Edg/"))||(Qb()?Pb("Opera"):F("OPR"))||Tb()||F("Silk")||F("Android"))&&!(Bc()||F("iPad")||F("iPod"));var ue={},ve=null;function we(a,b){Qa(a);void 0===b&&(b=0);xe();b=ue[b];for(var c=Array(Math.floor(a.length/3)),d=b[64]||"",e=0,f=0;e<a.length-2;e+=3){var g=a[e],h=a[e+1],k=a[e+2],l=b[g>>2];g=b[(g&3)<<4|h>>4];h=b[(h&15)<<2|k>>6];k=b[k&63];c[f++]=""+l+g+h+k}l=0;k=d;switch(a.length-e){case 2:l=a[e+1],k=b[(l&15)<<2]||d;case 1:a=a[e],c[f]=""+b[a>>2]+b[(a&3)<<4|l>>4]+k+d}return c.join("")}
function ye(a){var b=a.length,c=3*b/4;c%3?c=Math.floor(c):-1!="=.".indexOf(a[b-1])&&(c=-1!="=.".indexOf(a[b-2])?c-2:c-1);var d=new Uint8Array(c),e=0;ze(a,function(f){d[e++]=f});
return e!==c?d.subarray(0,e):d}
function ze(a,b){function c(k){for(;d<a.length;){var l=a.charAt(d++),n=ve[l];if(null!=n)return n;if(!/^[\s\xa0]*$/.test(l))throw Error("Unknown base64 encoding at char: "+l);}return k}
xe();for(var d=0;;){var e=c(-1),f=c(0),g=c(64),h=c(64);if(64===h&&-1===e)break;b(e<<2|f>>4);64!=g&&(b(f<<4&240|g>>2),64!=h&&b(g<<6&192|h))}}
function xe(){if(!ve){ve={};for(var a="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789".split(""),b=["+/=","+/","-_=","-_.","-_"],c=0;5>c;c++){var d=a.concat(b[c].split(""));ue[c]=d;for(var e=0;e<d.length;e++){var f=d[e];void 0===ve[f]&&(ve[f]=e)}}}}
;var Ae="undefined"!==typeof Uint8Array,Be=!Ec&&"function"===typeof btoa;function Ce(a){if(!Be)return we(a);for(var b="",c=0,d=a.length-10240;c<d;)b+=String.fromCharCode.apply(null,a.subarray(c,c+=10240));b+=String.fromCharCode.apply(null,c?a.subarray(c):a);return btoa(b)}
var De=/[-_.]/g,Ee={"-":"+",_:"/",".":"="};function Fe(a){return Ee[a]||""}
function Ge(a){return Ae&&null!=a&&a instanceof Uint8Array}
var He={};var Ie;function Je(a){if(a!==He)throw Error("illegal external caller");}
function Ke(a,b){Je(b);this.h=a;if(null!=a&&0===a.length)throw Error("ByteString should be constructed with non-empty values");}
Ke.prototype.sizeBytes=function(){Je(He);var a=this.h;if(null!=a&&!Ge(a))if("string"===typeof a)if(Be){De.test(a)&&(a=a.replace(De,Fe));a=atob(a);for(var b=new Uint8Array(a.length),c=0;c<a.length;c++)b[c]=a.charCodeAt(c);a=b}else a=ye(a);else Pa(a),a=null;return(a=null==a?a:this.h=a)?a.length:0};function Le(){return"function"===typeof BigInt}
;function Me(a){return Array.prototype.slice.call(a)}
;var Ne;Ne="function"===typeof Symbol&&"symbol"===typeof Symbol()?Symbol():void 0;Math.max.apply(Math,oa(Object.values({Lf:1,Jf:2,If:4,Of:8,Nf:16,Mf:32,zf:64,Qf:128,Hf:256,Gf:512,Kf:1024,Ef:2048,Pf:4096,Ff:8192})));var Oe=Ne?function(a,b){a[Ne]|=b}:function(a,b){void 0!==a.Sa?a.Sa|=b:Object.defineProperties(a,{Sa:{value:b,
configurable:!0,writable:!0,enumerable:!1}})};
function Pe(a,b,c){return c?a|b:a&~b}
var Qe=Ne?function(a){return a[Ne]|0}:function(a){return a.Sa|0},Re=Ne?function(a){return a[Ne]}:function(a){return a.Sa},Se=Ne?function(a,b){a[Ne]=b;
return a}:function(a,b){void 0!==a.Sa?a.Sa=b:Object.defineProperties(a,{Sa:{value:b,
configurable:!0,writable:!0,enumerable:!1}});return a};
function Te(a,b){Se(b,(a|0)&-14591)}
function Ue(a,b){Se(b,(a|34)&-14557)}
function Ve(a){a=a>>14&1023;return 0===a?536870912:a}
;var We={},Xe={};function Ye(a){return!(!a||"object"!==typeof a||a.h!==Xe)}
function Ze(a){return null!==a&&"object"===typeof a&&!Array.isArray(a)&&a.constructor===Object}
var $e;function af(a,b,c){if(!Array.isArray(a)||a.length)return!1;var d=Qe(a);if(d&1)return!0;if(!(b&&(Array.isArray(b)?b.includes(c):b.has(c))))return!1;Se(a,d|1);return!0}
var bf,cf=[];Se(cf,55);bf=Object.freeze(cf);function df(a){if(a&2)throw Error();}
Object.freeze(new function(){});
Object.freeze(new function(){});var ef=0,ff=0;function gf(a){var b=0>a;a=Math.abs(a);var c=a>>>0;a=Math.floor((a-c)/4294967296);b&&(c=v(hf(c,a)),b=c.next().value,a=c.next().value,c=b);ef=c>>>0;ff=a>>>0}
function jf(a,b){b>>>=0;a>>>=0;if(2097151>=b)var c=""+(4294967296*b+a);else Le()?c=""+(BigInt(b)<<BigInt(32)|BigInt(a)):(c=(a>>>24|b<<8)&16777215,b=b>>16&65535,a=(a&16777215)+6777216*c+6710656*b,c+=8147497*b,b*=2,1E7<=a&&(c+=Math.floor(a/1E7),a%=1E7),1E7<=c&&(b+=Math.floor(c/1E7),c%=1E7),c=b+kf(c)+kf(a));return c}
function kf(a){a=String(a);return"0000000".slice(a.length)+a}
function lf(){var a=ef,b=ff;b&2147483648?Le()?a=""+(BigInt(b|0)<<BigInt(32)|BigInt(a>>>0)):(b=v(hf(a,b)),a=b.next().value,b=b.next().value,a="-"+jf(a,b)):a=jf(a,b);return a}
function hf(a,b){b=~b;a?a=~a+1:b+=1;return[a,b]}
;function mf(a){a=Error(a);a.__closure__error__context__984382||(a.__closure__error__context__984382={});a.__closure__error__context__984382.severity="warning";return a}
;function nf(a){return a.displayName||a.name||"unknown type name"}
function of(a){if(null!=a&&"boolean"!==typeof a)throw Error("Expected boolean but got "+Pa(a)+": "+a);return a}
var pf=/^-?([1-9][0-9]*|0)(\.[0-9]+)?$/;function qf(a){var b=typeof a;return"number"===b?Number.isFinite(a):"string"!==b?!1:pf.test(a)}
function rf(a){if(null!=a){if("number"!==typeof a)throw mf("int32");if(!Number.isFinite(a))throw mf("int32");a|=0}return a}
function sf(a){if(null==a)return a;if("string"===typeof a){if(!a)return;a=+a}if("number"===typeof a)return Number.isFinite(a)?a|0:void 0}
function tf(a){if(null!=a){var b=!!b;if(!qf(a))throw mf("int64");a="string"===typeof a?uf(a):b?vf(a):wf(a)}return a}
function xf(a){return"-"===a[0]?20>a.length?!0:20===a.length&&-922337<Number(a.substring(0,7)):19>a.length?!0:19===a.length&&922337>Number(a.substring(0,6))}
function wf(a){qf(a);a=Math.trunc(a);if(!Number.isSafeInteger(a)){gf(a);var b=ef,c=ff;if(a=c&2147483648)b=~b+1>>>0,c=~c>>>0,0==b&&(c=c+1>>>0);b=4294967296*c+(b>>>0);a=a?-b:b}return a}
function vf(a){qf(a);a=Math.trunc(a);if(Number.isSafeInteger(a))a=String(a);else{var b=String(a);xf(b)?a=b:(gf(a),a=lf())}return a}
function uf(a){qf(a);var b=Math.trunc(Number(a));if(Number.isSafeInteger(b))return String(b);b=a.indexOf(".");-1!==b&&(a=a.substring(0,b));a.indexOf(".");if(!xf(a)){if(16>a.length)gf(Number(a));else if(Le())a=BigInt(a),ef=Number(a&BigInt(4294967295))>>>0,ff=Number(a>>BigInt(32)&BigInt(4294967295));else{b=+("-"===a[0]);ff=ef=0;for(var c=a.length,d=0+b,e=(c-b)%6+b;e<=c;d=e,e+=6)d=Number(a.slice(d,e)),ff*=1E6,ef=1E6*ef+d,4294967296<=ef&&(ff+=Math.trunc(ef/4294967296),ff>>>=0,ef>>>=0);b&&(b=v(hf(ef,ff)),
a=b.next().value,b=b.next().value,ef=a,ff=b)}a=lf()}return a}
function yf(a){if(null!=a&&"string"!==typeof a)throw Error();return a}
function zf(a,b){if(!(a instanceof b))throw Error("Expected instanceof "+nf(b)+" but got "+(a&&nf(a.constructor)));}
function Af(a,b,c){if(null!=a&&"object"===typeof a&&a.Jc===We)return a;if(Array.isArray(a)){var d=Qe(a),e=d;0===e&&(e|=c&32);e|=c&2;e!==d&&Se(a,e);return new b(a)}}
;var Bf;function Cf(a,b){Qe(b);Bf=b;a=new a(b);Bf=void 0;return a}
function I(a,b,c){null==a&&(a=Bf);Bf=void 0;if(null==a){var d=96;c?(a=[c],d|=512):a=[];b&&(d=d&-16760833|(b&1023)<<14)}else{if(!Array.isArray(a))throw Error();d=Qe(a);if(d&64)return a;d|=64;if(c&&(d|=512,c!==a[0]))throw Error();a:{c=a;var e=c.length;if(e){var f=e-1;if(Ze(c[f])){d|=256;b=f-(+!!(d&512)-1);if(1024<=b)throw Error();d=d&-16760833|(b&1023)<<14;break a}}if(b){b=Math.max(b,e-(+!!(d&512)-1));if(1024<b)throw Error();d=d&-16760833|(b&1023)<<14}}}Se(a,d);return a}
;function Df(a,b){return Ef(b)}
function Ef(a){switch(typeof a){case "number":return isFinite(a)?a:String(a);case "boolean":return a?1:0;case "object":if(a)if(Array.isArray(a)){if(af(a,void 0,0))return}else{if(Ge(a))return Ce(a);if(a instanceof Ke){var b=a.h;return null==b?"":"string"===typeof b?b:a.h=Ce(b)}}}return a}
;function Ff(a,b,c){a=Me(a);var d=a.length,e=b&256?a[d-1]:void 0;d+=e?-1:0;for(b=b&512?1:0;b<d;b++)a[b]=c(a[b]);if(e){b=a[b]={};for(var f in e)b[f]=c(e[f])}return a}
function Gf(a,b,c,d,e){if(null!=a){if(Array.isArray(a))a=af(a,void 0,0)?void 0:e&&Qe(a)&2?a:Hf(a,b,c,void 0!==d,e);else if(Ze(a)){var f={},g;for(g in a)f[g]=Gf(a[g],b,c,d,e);a=f}else a=b(a,d);return a}}
function Hf(a,b,c,d,e){var f=d||c?Qe(a):0;d=d?!!(f&32):void 0;a=Me(a);for(var g=0;g<a.length;g++)a[g]=Gf(a[g],b,c,d,e);c&&c(f,a);return a}
function If(a){return a.Jc===We?a.toJSON():Ef(a)}
;function Jf(a,b,c){c=void 0===c?Ue:c;if(null!=a){if(Ae&&a instanceof Uint8Array)return b?a:new Uint8Array(a);if(Array.isArray(a)){var d=Qe(a);if(d&2)return a;b&&(b=0===d||!!(d&32)&&!(d&64||!(d&16)));return b?Se(a,(d|34)&-12293):Hf(a,Jf,d&4?Ue:c,!0,!0)}a.Jc===We&&(c=a.F,d=Re(c),a=d&2?a:Cf(a.constructor,Kf(c,d,!0)));return a}}
function Kf(a,b,c){var d=c||b&2?Ue:Te,e=!!(b&32);a=Ff(a,b,function(f){return Jf(f,e,d)});
Oe(a,32|(c?2:0));return a}
function Lf(a){var b=a.F,c=Re(b);return c&2?Cf(a.constructor,Kf(b,c,!1)):a}
;function Mf(a,b){a=a.F;return Nf(a,Re(a),b)}
function Nf(a,b,c,d){if(-1===c)return null;if(c>=Ve(b)){if(b&256)return a[a.length-1][c]}else{var e=a.length;if(d&&b&256&&(d=a[e-1][c],null!=d))return d;b=c+(+!!(b&512)-1);if(b<e)return a[b]}}
function Of(a,b,c){var d=a.F,e=Re(d);df(e);Pf(d,e,b,c);return a}
function Pf(a,b,c,d,e){Ze(d);var f=Ve(b);if(c>=f||e){var g=b;if(b&256)e=a[a.length-1];else{if(null==d)return g;e=a[f+(+!!(b&512)-1)]={};g|=256}e[c]=d;c<f&&(a[c+(+!!(b&512)-1)]=void 0);g!==b&&Se(a,g);return g}a[c+(+!!(b&512)-1)]=d;b&256&&(a=a[a.length-1],c in a&&delete a[c]);return b}
function Qf(a){return void 0!==Rf(a,Sf,11,!1)}
function Tf(a){return!!(2&a)&&!!(4&a)||!!(2048&a)}
function Uf(a,b,c,d){a=a.F;var e=Re(a);df(e);for(var f=e,g=0,h=0;h<c.length;h++){var k=c[h];null!=Nf(a,f,k)&&(0!==g&&(f=Pf(a,f,g)),g=k)}(c=g)&&c!==b&&null!=d&&(e=Pf(a,e,c));Pf(a,e,b,d)}
function Rf(a,b,c,d){a=a.F;var e=Re(a),f=Nf(a,e,c,d);b=Af(f,b,e);b!==f&&null!=b&&Pf(a,e,c,b,d);return b}
function Vf(a,b,c,d){d=void 0===d?!1:d;b=Rf(a,b,c,d);if(null==b)return b;a=a.F;var e=Re(a);if(!(e&2)){var f=Lf(b);f!==b&&(b=f,Pf(a,e,c,b,d))}return b}
function Wf(a,b,c,d){null!=d?zf(d,b):d=void 0;return Of(a,c,d)}
function Xf(a,b,c,d){var e=a.F,f=Re(e);df(f);if(null==d)return Pf(e,f,c),a;if(!Array.isArray(d))throw mf();for(var g=Qe(d),h=g,k=!!(2&g)||!!(2048&g),l=k||Object.isFrozen(d),n=!l&&!1,p=!0,r=!0,t=0;t<d.length;t++){var x=d[t];zf(x,b);k||(x=!!(Qe(x.F)&2),p&&(p=!x),r&&(r=x))}k||(g=Pe(g,5,!0),g=Pe(g,8,p),g=Pe(g,16,r));if(n||l&&g!==h)d=Me(d),h=0,g=Yf(g,f,!0);g!==h&&Se(d,g);Pf(e,f,c,d);return a}
function Yf(a,b,c){a=Pe(a,2,!!(2&b));a=Pe(a,32,!!(32&b)&&c);return a=Pe(a,2048,!1)}
function Zf(a,b){a=Mf(a,b);var c;null==a?c=a:qf(a)?"number"===typeof a?c=wf(a):c=uf(a):c=void 0;return c}
function $f(a){a=Mf(a,1);var b=void 0===b?!1:b;b=null==a?a:qf(a)?"string"===typeof a?uf(a):b?vf(a):wf(a):void 0;return b}
function ag(a){a=Mf(a,1);return null==a?a:Number.isFinite(a)?a|0:void 0}
function bg(a,b,c){return Of(a,b,yf(c))}
function cg(a,b,c){if(null!=c){if(!Number.isFinite(c))throw mf("enum");c|=0}return Of(a,b,c)}
;function K(a,b,c){this.F=I(a,b,c)}
m=K.prototype;m.toJSON=function(){if($e)var a=dg(this,this.F,!1);else a=Hf(this.F,If,void 0,void 0,!1),a=dg(this,a,!0);return a};
m.serialize=function(){$e=!0;try{return JSON.stringify(this.toJSON(),Df)}finally{$e=!1}};
function eg(a,b){if(null==b||""==b)return new a;b=JSON.parse(b);if(!Array.isArray(b))throw Error(void 0);Oe(b,32);return Cf(a,b)}
m.clone=function(){var a=this.F,b=Re(a);return Cf(this.constructor,Kf(a,b,!1))};
m.Jc=We;m.toString=function(){return dg(this,this.F,!1).toString()};
function dg(a,b,c){var d=Lb?void 0:a.constructor.Ua;var e=Re(c?a.F:b);a=b.length;if(!a)return b;var f;if(Ze(c=b[a-1])){a:{var g=c;var h={},k=!1,l;for(l in g){var n=g[l];if(Array.isArray(n)){var p=n;if(af(n,d,+l)||Ye(n)&&0===n.size)n=null;n!=p&&(k=!0)}null!=n?h[l]=n:k=!0}if(k){for(var r in h){g=h;break a}g=null}}g!=c&&(f=!0);a--}for(l=+!!(e&512)-1;0<a;a--){r=a-1;c=b[r];r-=l;if(!(null==c||af(c,d,r)||Ye(c)&&0===c.size))break;var t=!0}if(!f&&!t)return b;b=Array.prototype.slice.call(b,0,a);g&&b.push(g);
return b}
;function fg(a){this.F=I(a)}
w(fg,K);var gg=[1,2,3];function hg(a){this.F=I(a)}
w(hg,K);var ig=[1,2,3];function jg(a){this.F=I(a)}
w(jg,K);jg.Ua=[1];function kg(a){this.F=I(a)}
w(kg,K);kg.Ua=[3,6,4];function lg(a){this.F=I(a)}
w(lg,K);lg.Ua=[1];function mg(a){if(!a)return"";if(/^about:(?:blank|srcdoc)$/.test(a))return window.origin||"";0===a.indexOf("blob:")&&(a=a.substring(5));a=a.split("#")[0].split("?")[0];a=a.toLowerCase();0==a.indexOf("//")&&(a=window.location.protocol+a);/^[\w\-]*:\/\//.test(a)||(a=window.location.href);var b=a.substring(a.indexOf("://")+3),c=b.indexOf("/");-1!=c&&(b=b.substring(0,c));c=a.substring(0,a.indexOf("://"));if(!c)throw Error("URI is missing protocol: "+a);if("http"!==c&&"https"!==c&&"chrome-extension"!==
c&&"moz-extension"!==c&&"file"!==c&&"android-app"!==c&&"chrome-search"!==c&&"chrome-untrusted"!==c&&"chrome"!==c&&"app"!==c&&"devtools"!==c)throw Error("Invalid URI scheme in origin: "+c);a="";var d=b.indexOf(":");if(-1!=d){var e=b.substring(d+1);b=b.substring(0,d);if("http"===c&&"80"!==e||"https"===c&&"443"!==e)a=":"+e}return c+"://"+b+a}
;function ng(){function a(){e[0]=1732584193;e[1]=4023233417;e[2]=2562383102;e[3]=271733878;e[4]=3285377520;n=l=0}
function b(p){for(var r=g,t=0;64>t;t+=4)r[t/4]=p[t]<<24|p[t+1]<<16|p[t+2]<<8|p[t+3];for(t=16;80>t;t++)p=r[t-3]^r[t-8]^r[t-14]^r[t-16],r[t]=(p<<1|p>>>31)&4294967295;p=e[0];var x=e[1],z=e[2],y=e[3],J=e[4];for(t=0;80>t;t++){if(40>t)if(20>t){var G=y^x&(z^y);var M=1518500249}else G=x^z^y,M=1859775393;else 60>t?(G=x&z|y&(x|z),M=2400959708):(G=x^z^y,M=3395469782);G=((p<<5|p>>>27)&4294967295)+G+J+M+r[t]&4294967295;J=y;y=z;z=(x<<30|x>>>2)&4294967295;x=p;p=G}e[0]=e[0]+p&4294967295;e[1]=e[1]+x&4294967295;e[2]=
e[2]+z&4294967295;e[3]=e[3]+y&4294967295;e[4]=e[4]+J&4294967295}
function c(p,r){if("string"===typeof p){p=unescape(encodeURIComponent(p));for(var t=[],x=0,z=p.length;x<z;++x)t.push(p.charCodeAt(x));p=t}r||(r=p.length);t=0;if(0==l)for(;t+64<r;)b(p.slice(t,t+64)),t+=64,n+=64;for(;t<r;)if(f[l++]=p[t++],n++,64==l)for(l=0,b(f);t+64<r;)b(p.slice(t,t+64)),t+=64,n+=64}
function d(){var p=[],r=8*n;56>l?c(h,56-l):c(h,64-(l-56));for(var t=63;56<=t;t--)f[t]=r&255,r>>>=8;b(f);for(t=r=0;5>t;t++)for(var x=24;0<=x;x-=8)p[r++]=e[t]>>x&255;return p}
for(var e=[],f=[],g=[],h=[128],k=1;64>k;++k)h[k]=0;var l,n;a();return{reset:a,update:c,digest:d,Wd:function(){for(var p=d(),r="",t=0;t<p.length;t++)r+="0123456789ABCDEF".charAt(Math.floor(p[t]/16))+"0123456789ABCDEF".charAt(p[t]%16);return r}}}
;function og(a,b,c){var d=String(C.location.href);return d&&a&&b?[b,pg(mg(d),a,c||null)].join(" "):null}
function pg(a,b,c){var d=[],e=[];if(1==(Array.isArray(c)?2:1))return e=[b,a],gb(d,function(h){e.push(h)}),qg(e.join(" "));
var f=[],g=[];gb(c,function(h){g.push(h.key);f.push(h.value)});
c=Math.floor((new Date).getTime()/1E3);e=0==f.length?[c,b,a]:[f.join(":"),c,b,a];gb(d,function(h){e.push(h)});
a=qg(e.join(" "));a=[c,a];0==g.length||a.push(g.join(""));return a.join("_")}
function qg(a){var b=ng();b.update(a);return b.Wd().toLowerCase()}
;var rg={};function sg(a){this.h=a||{cookie:""}}
m=sg.prototype;m.isEnabled=function(){if(!C.navigator.cookieEnabled)return!1;if(this.h.cookie)return!0;this.set("TESTCOOKIESENABLED","1",{Kb:60});if("1"!==this.get("TESTCOOKIESENABLED"))return!1;this.remove("TESTCOOKIESENABLED");return!0};
m.set=function(a,b,c){var d=!1;if("object"===typeof c){var e=c.Oe;d=c.secure||!1;var f=c.domain||void 0;var g=c.path||void 0;var h=c.Kb}if(/[;=\s]/.test(a))throw Error('Invalid cookie name "'+a+'"');if(/[;\r\n]/.test(b))throw Error('Invalid cookie value "'+b+'"');void 0===h&&(h=-1);c=f?";domain="+f:"";g=g?";path="+g:"";d=d?";secure":"";h=0>h?"":0==h?";expires="+(new Date(1970,1,1)).toUTCString():";expires="+(new Date(Date.now()+1E3*h)).toUTCString();this.h.cookie=a+"="+b+c+g+h+d+(null!=e?";samesite="+
e:"")};
m.get=function(a,b){for(var c=a+"=",d=(this.h.cookie||"").split(";"),e=0,f;e<d.length;e++){f=Jb(d[e]);if(0==f.lastIndexOf(c,0))return f.slice(c.length);if(f==a)return""}return b};
m.remove=function(a,b,c){var d=void 0!==this.get(a);this.set(a,"",{Kb:0,path:b,domain:c});return d};
m.Ac=function(){return tg(this).keys};
m.clear=function(){for(var a=tg(this).keys,b=a.length-1;0<=b;b--)this.remove(a[b])};
function tg(a){a=(a.h.cookie||"").split(";");for(var b=[],c=[],d,e,f=0;f<a.length;f++)e=Jb(a[f]),d=e.indexOf("="),-1==d?(b.push(""),c.push(e)):(b.push(e.substring(0,d)),c.push(e.substring(d+1)));return{keys:b,values:c}}
var ug=new sg("undefined"==typeof document?null:document);function vg(a){return!!rg.FPA_SAMESITE_PHASE2_MOD||!(void 0===a||!a)}
function wg(a){a=void 0===a?!1:a;var b=C.__SAPISID||C.__APISID||C.__3PSAPISID||C.__OVERRIDE_SID;vg(a)&&(b=b||C.__1PSAPISID);if(b)return!0;if("undefined"!==typeof document){var c=new sg(document);b=c.get("SAPISID")||c.get("APISID")||c.get("__Secure-3PAPISID")||c.get("SID")||c.get("OSID");vg(a)&&(b=b||c.get("__Secure-1PAPISID"))}return!!b}
function xg(a,b,c,d){(a=C[a])||"undefined"===typeof document||(a=(new sg(document)).get(b));return a?og(a,c,d):null}
function yg(a,b){b=void 0===b?!1:b;var c=mg(String(C.location.href)),d=[];if(wg(b)){c=0==c.indexOf("https:")||0==c.indexOf("chrome-extension:")||0==c.indexOf("moz-extension:");var e=c?C.__SAPISID:C.__APISID;e||"undefined"===typeof document||(e=new sg(document),e=e.get(c?"SAPISID":"APISID")||e.get("__Secure-3PAPISID"));(e=e?og(e,c?"SAPISIDHASH":"APISIDHASH",a):null)&&d.push(e);c&&vg(b)&&((b=xg("__1PSAPISID","__Secure-1PAPISID","SAPISID1PHASH",a))&&d.push(b),(a=xg("__3PSAPISID","__Secure-3PAPISID",
"SAPISID3PHASH",a))&&d.push(a))}return 0==d.length?null:d.join(" ")}
;function zg(a){this.F=I(a)}
w(zg,K);zg.Ua=[2];function Ag(a){od.call(this);this.intervalMs=a;this.enabled=!1;this.i=function(){return Za()};
this.j=this.i()}
w(Ag,od);Ag.prototype.setInterval=function(a){this.intervalMs=a;this.timer&&this.enabled?(this.stop(),this.start()):this.timer&&this.stop()};
Ag.prototype.start=function(){var a=this;this.enabled=!0;this.timer||(this.timer=setTimeout(function(){a.tick()},this.intervalMs),this.j=this.i())};
Ag.prototype.stop=function(){this.enabled=!1;this.timer&&(clearTimeout(this.timer),this.timer=void 0)};
Ag.prototype.tick=function(){var a=this;if(this.enabled){var b=Math.max(this.i()-this.j,0);b<.8*this.intervalMs?this.timer=setTimeout(function(){a.tick()},this.intervalMs-b):(this.timer&&(clearTimeout(this.timer),this.timer=void 0),pd(this,"tick"),this.enabled&&(this.stop(),this.start()))}else this.timer=void 0};function Bg(a){this.F=I(a)}
w(Bg,K);function Cg(a){this.F=I(a)}
w(Cg,K);function Dg(a){this.h=this.i=this.j=a}
Dg.prototype.reset=function(){this.h=this.i=this.j};
Dg.prototype.getValue=function(){return this.i};function Eg(a){this.F=I(a)}
w(Eg,K);Eg.prototype.Bc=function(){return ag(this)};function Fg(a){this.F=I(a)}
w(Fg,K);function Gg(a){this.F=I(a)}
w(Gg,K);function Hg(a,b){Xf(a,Fg,1,b)}
Gg.Ua=[1];function Sf(a){this.F=I(a)}
w(Sf,K);var Ig=["platform","platformVersion","architecture","model","uaFullVersion"],Jg=new Gg,Kg=null;function Lg(a,b){b=void 0===b?Ig:b;if(!Kg){var c;a=null==(c=a.navigator)?void 0:c.userAgentData;if(!a||"function"!==typeof a.getHighEntropyValues)return Promise.reject(Error("UACH unavailable"));c=(a.brands||[]).map(function(d){var e=new Fg;e=bg(e,1,d.brand);return bg(e,2,d.version)});
Hg(Of(Jg,2,of(a.mobile)),c);Kg=a.getHighEntropyValues(b)}return Kg.then(function(d){var e=Jg.clone();b.includes("platform")&&bg(e,3,d.platform);b.includes("platformVersion")&&bg(e,4,d.platformVersion);b.includes("architecture")&&bg(e,5,d.architecture);b.includes("model")&&bg(e,6,d.model);b.includes("uaFullVersion")&&bg(e,7,d.uaFullVersion);return e}).catch(function(){return Jg.clone()})}
;function Mg(a){this.F=I(a)}
w(Mg,K);function Ng(a){this.F=I(a,4)}
w(Ng,K);function Og(a){this.F=I(a,35)}
w(Og,K);Og.Ua=[3,20,27];function Pg(a){this.F=I(a,19)}
w(Pg,K);Pg.prototype.Nb=function(a){return cg(this,2,a)};
Pg.Ua=[3,5];function Qg(a){this.F=I(a,7)}
w(Qg,K);var Sg=function(a){return function(b){return eg(a,b)}}(Qg);
Qg.Ua=[5,6];function Tg(a){this.F=I(a)}
w(Tg,K);var Ug=new function(a,b){this.h=a;this.ctor=b;this.isRepeated=0;this.i=Vf;this.defaultValue=void 0}(175237375,Tg);function Vg(a){H.call(this);var b=this;this.componentId="";this.j=[];this.ba="";this.ea=this.Y=-1;this.experimentIds=null;this.V=this.m=0;this.ha=1;this.timeoutMillis=0;this.logSource=a.logSource;this.Gb=a.Gb||function(){};
this.i=new Wg(a.logSource,a.eb);this.network=a.network;this.yb=a.yb||null;this.bufferSize=1E3;this.A=a.kf||null;this.sessionIndex=a.sessionIndex||null;this.Eb=a.Eb||!1;this.pageId=a.pageId||null;this.logger=null;this.withCredentials=!a.ed;this.eb=a.eb||!1;this.S="undefined"!==typeof URLSearchParams&&!!(new URL(Xg())).searchParams&&!!(new URL(Xg())).searchParams.set;var c=cg(new Mg,1,1);Yg(this.i,c);this.l=new Dg(1E4);this.h=new Ag(this.l.getValue());a=Zg(this,a.Xc);dd(this.h,"tick",a,!1,this);this.D=
new Ag(6E5);dd(this.D,"tick",a,!1,this);this.Eb||this.D.start();this.eb||(dd(document,"visibilitychange",function(){"hidden"===document.visibilityState&&b.vc()}),dd(document,"pagehide",this.vc,!1,this))}
w(Vg,H);function Zg(a,b){return a.S?b?function(){b().then(function(){a.flush()})}:function(){a.flush()}:function(){}}
m=Vg.prototype;m.R=function(){this.vc();this.h.stop();this.D.stop();H.prototype.R.call(this)};
m.log=function(a){if(this.S){a=a.clone();var b=this.ha++;a=Of(a,21,tf(b));this.componentId&&bg(a,26,this.componentId);if(!$f(a)){var c=Date.now();b=a;c=Number.isFinite(c)?c.toString():"0";Of(b,1,tf(c))}null==Zf(a,15)&&Of(a,15,tf(60*(new Date).getTimezoneOffset()));this.experimentIds&&(b=a,c=this.experimentIds.clone(),Wf(b,zg,16,c));b=this.j.length-this.bufferSize+1;0<b&&(this.j.splice(0,b),this.m+=b);this.j.push(a);this.Eb||this.h.enabled||this.h.start()}};
m.flush=function(a,b){var c=this;if(0===this.j.length)a&&a();else{var d=Date.now();if(this.ea>d&&this.Y<d)b&&b("throttled");else{this.network&&("function"===typeof this.network.Bc?$g(this.i,this.network.Bc()):$g(this.i,0));var e=ah(this.i,this.j,this.m,this.V,this.yb);d={};var f=this.Gb();f&&(d.Authorization=f);this.A||(this.A=Xg());try{var g=(new URL(this.A)).toString()}catch(k){g=(new URL(this.A,window.location.origin)).toString()}g=new URL(g);this.sessionIndex&&(d["X-Goog-AuthUser"]=this.sessionIndex,
g.searchParams.set("authuser",this.sessionIndex));this.pageId&&(d["X-Goog-PageId"]=this.pageId,g.searchParams.set("pageId",this.pageId));if(f&&this.ba===f)b&&b("stale-auth-token");else{this.j=[];this.h.enabled&&this.h.stop();this.m=0;var h=e.serialize();d={url:g.toString(),body:h,Tf:1,Je:d,requestType:"POST",withCredentials:this.withCredentials,timeoutMillis:this.timeoutMillis};g=function(k){c.l.reset();c.h.setInterval(c.l.getValue());if(k){var l=null;try{var n=JSON.stringify(JSON.parse(k.replace(")]}'\n",
"")));l=Sg(n)}catch(r){}if(l){k=Number;n="-1";n=void 0===n?"0":n;var p=$f(l);k=k(null!=p?p:n);0<k&&(c.Y=Date.now(),c.ea=c.Y+k);l=Ug.ctor?Ug.i(l,Ug.ctor,Ug.h,!0):Ug.i(l,Ug.h,null,!0);if(k=null===l?void 0:l)l=-1,l=void 0===l?0:l,k=sf(Mf(k,1)),l=null!=k?k:l,-1!==l&&(c.l=new Dg(1>l?1:l),c.h.setInterval(c.l.getValue()))}}a&&a();c.V=0};
h=function(k,l){var n=e.F;var p=Re(n),r=p,t=!(2&p),x=!!(2&r),z=x?1:2;p=1===z;z=2===z;t&&(t=!x);x=Nf(n,r,3);x=Array.isArray(x)?x:bf;var y=Qe(x),J=!!(4&y);if(!J){var G=y;0===G&&(G=Yf(G,r,!1));G=Pe(G,1,!0);y=x;var M=r,P=!!(2&G);P&&(M=Pe(M,2,!0));for(var ea=!P,aa=!0,U=0,fa=0;U<y.length;U++){var la=Af(y[U],Og,M);if(la instanceof Og){if(!P){var ma=!!(Qe(la.F)&2);ea&&(ea=!ma);aa&&(aa=ma)}y[fa++]=la}}fa<U&&(y.length=fa);G=Pe(G,4,!0);G=Pe(G,16,aa);G=Pe(G,8,ea);Se(y,G);P&&Object.freeze(y);y=G}G=!!(8&y)||p&&
!x.length;if(t&&!G){Tf(y)&&(x=Me(x),y=Yf(y,r,!1),r=Pf(n,r,3,x));t=x;for(G=0;G<t.length;G++)M=t[G],P=Lf(M),M!==P&&(t[G]=P);y=Pe(y,8,!0);y=Pe(y,16,!t.length);Se(t,y)}Tf(y)||(t=y,p?y=Pe(y,!x.length||16&y&&(!J||32&y)?2:2048,!0):y=Pe(y,32,!1),y!==t&&Se(x,y),p&&Object.freeze(x));z&&Tf(y)&&(x=Me(x),y=Yf(y,r,!1),Se(x,y),Pf(n,r,3,x));n=x;r=Zf(e,14);p=c.l;p.h=Math.min(3E5,2*p.h);p.i=Math.min(3E5,p.h+Math.round(.2*(Math.random()-.5)*p.h));c.h.setInterval(c.l.getValue());401===k&&f&&(c.ba=f);r&&(c.m+=r);void 0===
l&&(l=c.isRetryable(k));l&&(c.j=n.concat(c.j),c.Eb||c.h.enabled||c.h.start());b&&b("net-send-failed",k);++c.V};
c.network&&c.network.send(d,g,h)}}}};
m.vc=function(){bh(this.i,!0);this.flush();bh(this.i,!1)};
m.isRetryable=function(a){return 500<=a&&600>a||401===a||0===a};
function Xg(){return"https://play.google.com/log?format=json&hasfast=true"}
function Wg(a,b){this.eb=b=void 0===b?!1:b;this.uach=this.locale=null;this.h=new Pg;Number.isInteger(a)&&this.h.Nb(a);b||(this.locale=document.documentElement.getAttribute("lang"));Yg(this,new Mg)}
Wg.prototype.Nb=function(a){this.h.Nb(a);return this};
function Yg(a,b){Wf(a.h,Mg,1,b);ag(b)||cg(b,1,1);if(!a.eb){b=ch(a);var c=Mf(b,5);(null==c||"string"===typeof c)&&c||bg(b,5,a.locale)}a.uach&&(b=ch(a),Vf(b,Gg,9)||Wf(b,Gg,9,a.uach))}
function $g(a,b){Qf(dh(a))&&(a=eh(a),cg(a,1,b))}
function bh(a,b){Qf(dh(a))&&(a=eh(a),Of(a,2,of(b)))}
function dh(a){return Vf(a.h,Mg,1)}
function fh(a){var b=void 0===b?Ig:b;var c=a.eb?void 0:window;c?Lg(c,b).then(function(d){a.uach=d;d=ch(a);Wf(d,Gg,9,a.uach);return!0}).catch(function(){return!1}):Promise.resolve(!1)}
function ch(a){a=dh(a);var b=Vf(a,Sf,11);b||(b=new Sf,Wf(a,Sf,11,b));return b}
function eh(a){a=ch(a);var b=Vf(a,Eg,10);b||(b=new Eg,Of(b,2,of(!1)),Wf(a,Eg,10,b));return b}
function ah(a,b,c,d,e){var f=0,g=0;c=void 0===c?0:c;f=void 0===f?0:f;g=void 0===g?0:g;d=void 0===d?0:d;if(Qf(dh(a))){var h=eh(a);Of(h,3,rf(d))}Qf(dh(a))&&(d=eh(a),Of(d,4,rf(f)));Qf(dh(a))&&(f=eh(a),Of(f,5,rf(g)));a=a.h.clone();g=Date.now().toString();a=Of(a,4,tf(g));b=Xf(a,Og,3,b);e&&(a=new Bg,e=Of(a,13,rf(e)),a=new Cg,e=Wf(a,Bg,2,e),a=new Ng,e=Wf(a,Cg,1,e),e=cg(e,2,9),Wf(b,Ng,18,e));c&&Of(b,14,tf(c));return b}
;function gh(){}
gh.prototype.serialize=function(a){var b=[];hh(this,a,b);return b.join("")};
function hh(a,b,c){if(null==b)c.push("null");else{if("object"==typeof b){if(Array.isArray(b)){var d=b;b=d.length;c.push("[");for(var e="",f=0;f<b;f++)c.push(e),hh(a,d[f],c),e=",";c.push("]");return}if(b instanceof String||b instanceof Number||b instanceof Boolean)b=b.valueOf();else{c.push("{");e="";for(d in b)Object.prototype.hasOwnProperty.call(b,d)&&(f=b[d],"function"!=typeof f&&(c.push(e),ih(d,c),c.push(":"),hh(a,f,c),e=","));c.push("}");return}}switch(typeof b){case "string":ih(b,c);break;case "number":c.push(isFinite(b)&&
!isNaN(b)?String(b):"null");break;case "boolean":c.push(String(b));break;case "function":c.push("null");break;default:throw Error("Unknown type: "+typeof b);}}}
var jh={'"':'\\"',"\\":"\\\\","/":"\\/","\b":"\\b","\f":"\\f","\n":"\\n","\r":"\\r","\t":"\\t","\v":"\\u000b"},kh=/\uffff/.test("\uffff")?/[\\"\x00-\x1f\x7f-\uffff]/g:/[\\"\x00-\x1f\x7f-\xff]/g;function ih(a,b){b.push('"',a.replace(kh,function(c){var d=jh[c];d||(d="\\u"+(c.charCodeAt(0)|65536).toString(16).slice(1),jh[c]=d);return d}),'"')}
;function lh(){}
lh.prototype.h=null;lh.prototype.getOptions=function(){var a;(a=this.h)||(a={},mh(this)&&(a[0]=!0,a[1]=!0),a=this.h=a);return a};var nh;function oh(){}
$a(oh,lh);function ph(a){return(a=mh(a))?new ActiveXObject(a):new XMLHttpRequest}
function mh(a){if(!a.i&&"undefined"==typeof XMLHttpRequest&&"undefined"!=typeof ActiveXObject){for(var b=["MSXML2.XMLHTTP.6.0","MSXML2.XMLHTTP.3.0","MSXML2.XMLHTTP","Microsoft.XMLHTTP"],c=0;c<b.length;c++){var d=b[c];try{return new ActiveXObject(d),a.i=d}catch(e){}}throw Error("Could not create ActiveXObject. ActiveX might be disabled, or MSXML might not be installed");}return a.i}
nh=new oh;function qh(a){od.call(this);this.headers=new Map;this.V=a||null;this.i=!1;this.S=this.J=null;this.l=this.ea="";this.j=this.ba=this.A=this.Y=!1;this.m=0;this.D=null;this.Pa="";this.ta=this.Ba=!1}
$a(qh,od);var rh=/^https?$/i,sh=["POST","PUT"],th=[];function uh(a,b,c,d,e,f,g){var h=new qh;th.push(h);b&&h.listen("complete",b);h.h.add("ready",h.Ud,!0,void 0,void 0);f&&(h.m=Math.max(0,f));g&&(h.Ba=g);h.send(a,c,d,e)}
m=qh.prototype;m.Ud=function(){this.dispose();lb(th,this)};
m.send=function(a,b,c,d){if(this.J)throw Error("[goog.net.XhrIo] Object is active with another request="+this.ea+"; newUri="+a);b=b?b.toUpperCase():"GET";this.ea=a;this.l="";this.Y=!1;this.i=!0;this.J=this.V?ph(this.V):ph(nh);this.S=this.V?this.V.getOptions():nh.getOptions();this.J.onreadystatechange=Xa(this.rd,this);try{this.getStatus(),this.ba=!0,this.J.open(b,String(a),!0),this.ba=!1}catch(g){this.getStatus();vh(this,g);return}a=c||"";c=new Map(this.headers);if(d)if(Object.getPrototypeOf(d)===
Object.prototype)for(var e in d)c.set(e,d[e]);else if("function"===typeof d.keys&&"function"===typeof d.get){e=v(d.keys());for(var f=e.next();!f.done;f=e.next())f=f.value,c.set(f,d.get(f))}else throw Error("Unknown input type for opt_headers: "+String(d));d=Array.from(c.keys()).find(function(g){return"content-type"==g.toLowerCase()});
e=C.FormData&&a instanceof C.FormData;!(0<=fb(sh,b))||d||e||c.set("Content-Type","application/x-www-form-urlencoded;charset=utf-8");b=v(c);for(d=b.next();!d.done;d=b.next())c=v(d.value),d=c.next().value,c=c.next().value,this.J.setRequestHeader(d,c);this.Pa&&(this.J.responseType=this.Pa);"withCredentials"in this.J&&this.J.withCredentials!==this.Ba&&(this.J.withCredentials=this.Ba);try{wh(this),0<this.m&&(this.ta=xh(this.J),this.getStatus(),this.ta?(this.J.timeout=this.m,this.J.ontimeout=Xa(this.Hd,
this)):this.D=be(this.Hd,this.m,this)),this.getStatus(),this.A=!0,this.J.send(a),this.A=!1}catch(g){this.getStatus(),vh(this,g)}};
function xh(a){return Ec&&"number"===typeof a.timeout&&void 0!==a.ontimeout}
m.Hd=function(){"undefined"!=typeof Na&&this.J&&(this.l="Timed out after "+this.m+"ms, aborting",this.getStatus(),pd(this,"timeout"),this.abort(8))};
function vh(a,b){a.i=!1;a.J&&(a.j=!0,a.J.abort(),a.j=!1);a.l=b;yh(a);zh(a)}
function yh(a){a.Y||(a.Y=!0,pd(a,"complete"),pd(a,"error"))}
m.abort=function(){this.J&&this.i&&(this.getStatus(),this.i=!1,this.j=!0,this.J.abort(),this.j=!1,pd(this,"complete"),pd(this,"abort"),zh(this))};
m.R=function(){this.J&&(this.i&&(this.i=!1,this.j=!0,this.J.abort(),this.j=!1),zh(this,!0));qh.Aa.R.call(this)};
m.rd=function(){this.Z()||(this.ba||this.A||this.j?Ah(this):this.Ce())};
m.Ce=function(){Ah(this)};
function Ah(a){if(a.i&&"undefined"!=typeof Na)if(a.S[1]&&4==Bh(a)&&2==a.getStatus())a.getStatus();else if(a.A&&4==Bh(a))be(a.rd,0,a);else if(pd(a,"readystatechange"),a.isComplete()){a.getStatus();a.i=!1;try{if(Ch(a))pd(a,"complete"),pd(a,"success");else{try{var b=2<Bh(a)?a.J.statusText:""}catch(c){b=""}a.l=b+" ["+a.getStatus()+"]";yh(a)}}finally{zh(a)}}}
function zh(a,b){if(a.J){wh(a);var c=a.J,d=a.S[0]?function(){}:null;
a.J=null;a.S=null;b||pd(a,"ready");try{c.onreadystatechange=d}catch(e){}}}
function wh(a){a.J&&a.ta&&(a.J.ontimeout=null);a.D&&(C.clearTimeout(a.D),a.D=null)}
m.isActive=function(){return!!this.J};
m.isComplete=function(){return 4==Bh(this)};
function Ch(a){var b=a.getStatus();a:switch(b){case 200:case 201:case 202:case 204:case 206:case 304:case 1223:var c=!0;break a;default:c=!1}if(!c){if(b=0===b)a=bc(1,String(a.ea)),!a&&C.self&&C.self.location&&(a=C.self.location.protocol.slice(0,-1)),b=!rh.test(a?a.toLowerCase():"");c=b}return c}
function Bh(a){return a.J?a.J.readyState:0}
m.getStatus=function(){try{return 2<Bh(this)?this.J.status:-1}catch(a){return-1}};
m.getLastError=function(){return"string"===typeof this.l?this.l:String(this.l)};function Dh(){}
Dh.prototype.send=function(a,b,c){b=void 0===b?function(){}:b;
c=void 0===c?function(){}:c;
uh(a.url,function(d){d=d.target;if(Ch(d)){try{var e=d.J?d.J.responseText:""}catch(f){e=""}b(e)}else c(d.getStatus())},a.requestType,a.body,a.Je,a.timeoutMillis,a.withCredentials)};
Dh.prototype.Bc=function(){return 1};function Eh(a,b){H.call(this);this.logSource=a;this.sessionIndex=b;this.i="https://play.google.com/log?format=json&hasfast=true";this.h=null;this.j=!1;this.componentId="";this.yb=null;this.network=new Dh}
w(Eh,H);Eh.prototype.ed=function(){this.l=!0;return this};function Fh(a,b,c,d,e,f,g){a=void 0===a?-1:a;b=void 0===b?"":b;c=void 0===c?"":c;d=void 0===d?!1:d;e=void 0===e?"":e;H.call(this);this.logSource=a;this.componentId=b;f?a=f:(a=new Eh(a,"0"),a.componentId=b,tc(this,a),""!==c&&(a.i=c),d&&(a.j=!0),e&&(a.h=e),g&&(a.network=g),b=new Vg({logSource:a.logSource,Gb:a.Gb?a.Gb:yg,sessionIndex:a.sessionIndex,kf:a.i,eb:a.j,Eb:!1,ed:a.l,pageId:a.pageId,Xc:a.Xc,network:a.network?a.network:void 0}),tc(a,b),a.h&&(c=a.h,d=ch(b.i),bg(d,7,c)),a.componentId&&(b.componentId=
a.componentId),a.yb&&(b.yb=a.yb),fh(b.i),a.network.Nb&&a.network.Nb(a.logSource),a.network.Xe&&a.network.Xe(b),a=b);this.h=a}
w(Fh,H);
Fh.prototype.flush=function(a){var b=a||[];if(b.length){a=new lg;for(var c=[],d=0;d<b.length;d++){var e=b[d];var f=new kg;f=bg(f,1,e.l);for(var g=[],h=0;h<e.fields.length;h++)g.push(e.fields[h].na);h=f.F;var k=Re(h);df(k);if(null==g)Pf(h,k,3);else{if(!Array.isArray(g))throw mf();var l=Qe(g),n=l,p=!!(2&l)||Object.isFrozen(g),r=!p&&!1;var t=4&l?!1:!0;if(t)for(l=21,p&&(g=Me(g),n=0,l=Yf(l,k,!0)),t=0;t<g.length;t++){p=g;var x=t,z=g[t];if("string"!==typeof z)throw Error();p[x]=z}r&&(g=Me(g),n=0,l=Yf(l,
k,!0));l!==n&&Se(g,l);Pf(h,k,3,g)}g=[];h=[];k=v(e.h.keys());for(l=k.next();!l.done;l=k.next())h.push(l.value.split(","));for(k=0;k<h.length;k++){l=h[k];n=e.j;r=e.xc(l)||[];t=[];for(p=0;p<r.length;p++){z=(x=r[p])&&x.h;x=new hg;switch(n){case 3:z=Number(z);Number.isFinite(z)&&Uf(x,1,ig,tf(z));break;case 2:z=Number(z);if(null!=z&&"number"!==typeof z)throw Error("Value of float/double field must be a number, found "+typeof z+": "+z);Uf(x,2,ig,z)}t.push(x)}n=t;for(r=0;r<n.length;r++){t=n[r];p=new jg;t=
Wf(p,hg,2,t);p=l;x=[];z=[];for(var y=0;y<e.fields.length;y++)z.push(e.fields[y].oa);for(y=0;y<z.length;y++){var J=z[y],G=p[y],M=new fg;switch(J){case 3:Uf(M,1,gg,yf(String(G)));break;case 2:J=Number(G);Number.isFinite(J)&&Uf(M,2,gg,rf(J));break;case 1:Uf(M,3,gg,of("true"===G))}x.push(M)}Xf(t,fg,1,x);g.push(t)}}Xf(f,jg,4,g);c.push(f);e.clear()}Xf(a,kg,1,c);b=this.h;b.S&&(a instanceof Og?b.log(a):(c=new Og,a=a.serialize(),a=bg(c,8,a),b.log(a)));this.h.flush()}};function Gh(a,b,c){this.logger=a;this.event=b;if(void 0===c||c)this.h=Hh()}
Gh.prototype.start=function(){this.h=Hh()};
Gh.prototype.done=function(){null!=this.h&&this.logger.od(this.event,Hh()-this.h)};
function Ih(){}
Ih.prototype.Gc=function(){};
Ih.prototype.od=function(){};
Ih.prototype.ec=function(){};
Ih.prototype.Oa=function(){};
function Jh(a,b){this.i=b;this.l=new Fh(1828,"","",!1,"",void 0,new Dh);this.h=new ce(this.l);this.m=new ie(this.h);this.A=new le(this.h);this.D=new me(this.h);this.v=new he(this.h);new je(this.h);new ke(this.h);this.j=oe(a);(new ge(this.h)).h.oc("/client_streamz/bg/fic",this.i)}
Jh.prototype.Gc=function(){this.A.h.oc("/client_streamz/bg/fsc",this.j,this.i)};
Jh.prototype.od=function(a,b){0===a?this.m.record(b,this.j,this.i):1===a&&this.D.record(b,this.j,this.i)};
Jh.prototype.ec=function(a,b){this.v.h.oc("/client_streamz/bg/fiec",this.j,this.i,a,b)};
Jh.prototype.Oa=function(){this.h.Oa()};
function Hh(){var a,b,c;return null!=(c=null==(a=globalThis.performance)?void 0:null==(b=a.now)?void 0:b.call(a))?c:Date.now()}
;function Kh(){var a=this;this.promise=new Promise(function(b,c){a.resolve=b;a.reject=c})}
;function Lh(a){!1===a.xd||a.ga||(a.ga=function(b){var c;return new Jh(b,null!=(c=a.gg)?c:"_")});
return new Mh(a)}
function Mh(a){function b(l,n,p){Promise.resolve().then(function(){h.done();g.resolve({Rd:l,af:n,hg:p})})}
function c(){}
this.h=!1;var d=a.program;var e=a.ke;var f="function"===typeof a.ga?a.ga(e):a.ga;!1!==a.xd&&f||(f=new Ih);this.ga=f;var g=new Kh;this.i=g.promise;var h=new Gh(this.ga,0,!1);C[e]?C[e].a||(this.ga.ec(2,""),this.ga.Oa()):(this.ga.ec(1,""),this.ga.Oa());try{var k=C[e].a;h.start();this.j=v(k(d,b,!0,a.qg,c)).next().value;this.Ze=g.promise.then(function(){})}catch(l){throw this.ga.ec(4,l.message),this.ga.Oa(),l;
}}
Mh.prototype.snapshot=function(a){var b=this;if(this.h)throw Error("Already disposed");this.ga.Gc();return this.i.then(function(c){var d=c.Rd;return new Promise(function(e){var f=new Gh(b.ga,1);d(function(g){f.done();e(g)},[a.dd,
a.bf,a.mf,a.cf])})})};
Mh.prototype.Ed=function(a){if(this.h)throw Error("Already disposed");this.ga.Gc();var b=new Gh(this.ga,1);a=this.j([a.dd,a.bf,a.mf,a.cf]);b.done();return a};
Mh.prototype.dispose=function(){this.ga.Oa();this.h=!0;this.i.then(function(a){(a=a.af)&&a()})};
Mh.prototype.Z=function(){return this.h};var Nh=window;Cb("csi.gstatic.com");Cb("googleads.g.doubleclick.net");Cb("partner.googleadservices.com");Cb("pubads.g.doubleclick.net");Cb("securepubads.g.doubleclick.net");Cb("tpc.googlesyndication.com");var Oh=ka([""]),Ph=na(["\x00"],["\\0"]),Qh=na(["\n"],["\\n"]),Rh=na(["\x00"],["\\u0000"]);function Sh(a){return-1===a.toString().indexOf("`")}
Sh(function(a){return a(Oh)})||Sh(function(a){return a(Ph)})||Sh(function(a){return a(Qh)})||Sh(function(a){return a(Rh)});function Th(a){this.te=a}
function Uh(a){return new Th(function(b){return b.substr(0,a.length+1).toLowerCase()===a+":"})}
var Vh=[Uh("data"),Uh("http"),Uh("https"),Uh("mailto"),Uh("ftp"),new Th(function(a){return/^[^:]*([/?#]|$)/.test(a)})],Wh=/^\s*(?!javascript:)(?:[a-z0-9+.-]+:|[^:\/?#]*(?:[\/?#]|$))/i;
function Xh(a){a instanceof Hb?a instanceof Hb&&a.constructor===Hb?a=a.h:(Pa(a),a="type_error:SafeUrl"):a=Wh.test(a)?a:void 0;return a}
;function Yh(a,b){b=Xh(b);void 0!==b&&(a.href=b)}
;function Zh(){}
function $h(a){this.h=a}
w($h,Zh);$h.prototype.toString=function(){return this.h};function ai(a){var b="true".toString(),c=[new $h(bi[0].toLowerCase(),Wb)];if(0===c.length)throw Error("");if(c.map(function(d){if(d instanceof $h)d=d.h;else throw Error("");return d}).every(function(d){return 0!=="data-loaded".indexOf(d)}))throw Error('Attribute "data-loaded" does not match any of the allowed prefixes.');
a.setAttribute("data-loaded",b)}
;function ci(){throw Error("unknown trace type");}
;var di="alternate author bookmark canonical cite help icon license modulepreload next prefetch dns-prefetch prerender preconnect preload prev search subresource".split(" ");function ei(a,b){if(b instanceof Db)a.href=Eb(b).toString();else{if(-1===di.indexOf("stylesheet"))throw Error('TrustedResourceUrl href attribute required with rel="stylesheet"');b=Xh(b);if(void 0===b)return;a.href=b}a.rel="stylesheet"}
;function fi(a){var b,c;return(a=null==(c=(b=a.document).querySelector)?void 0:c.call(b,"script[nonce]"))?a.nonce||a.getAttribute("nonce")||"":""}
;function gi(a){var b=fi(a.ownerDocument&&a.ownerDocument.defaultView||window);b&&a.setAttribute("nonce",b)}
function hi(a,b){if(b instanceof Xb)b=b.ud;else throw Error("");a.textContent=b;gi(a)}
function ii(a,b){a.src=Eb(b);gi(a)}
;function ji(a){var b=ki;if(b)for(var c in b)Object.prototype.hasOwnProperty.call(b,c)&&a(b[c],c,b)}
function li(){var a=[];ji(function(b){a.push(b)});
return a}
var ki={nf:"allow-forms",pf:"allow-modals",qf:"allow-orientation-lock",rf:"allow-pointer-lock",sf:"allow-popups",tf:"allow-popups-to-escape-sandbox",uf:"allow-presentation",vf:"allow-same-origin",wf:"allow-scripts",xf:"allow-top-navigation",yf:"allow-top-navigation-by-user-activation"},mi=eb(function(){return li()});
function ni(){var a=oi(),b={};gb(mi(),function(c){a.sandbox&&a.sandbox.supports&&a.sandbox.supports(c)&&(b[c]=!0)});
return b}
function oi(){var a=void 0===a?document:a;return a.createElement("iframe")}
;"ARTICLE SECTION NAV ASIDE H1 H2 H3 H4 H5 H6 HEADER FOOTER ADDRESS P HR PRE BLOCKQUOTE OL UL LH LI DL DT DD FIGURE FIGCAPTION MAIN DIV EM STRONG SMALL S CITE Q DFN ABBR RUBY RB RT RTC RP DATA TIME CODE VAR SAMP KBD SUB SUP I B U MARK BDI BDO SPAN BR WBR INS DEL PICTURE PARAM TRACK MAP TABLE CAPTION COLGROUP COL TBODY THEAD TFOOT TR TD TH SELECT DATALIST OPTGROUP OPTION OUTPUT PROGRESS METER FIELDSET LEGEND DETAILS SUMMARY MENU DIALOG SLOT CANVAS FONT CENTER ACRONYM BASEFONT BIG DIR HGROUP STRIKE TT".split(" ").concat(["BUTTON"]);function pi(a){"number"==typeof a&&(a=Math.round(a)+"px");return a}
;var qi=(new Date).getTime();function ri(a){od.call(this);var b=this;this.A=this.j=0;this.Da=null!=a?a:{pa:function(e,f){return setTimeout(e,f)},
qa:function(e){clearTimeout(e)}};
var c,d;this.i=null!=(d=null==(c=window.navigator)?void 0:c.onLine)?d:!0;this.l=function(){return A(function(e){return e.yield(si(b),0)})};
window.addEventListener("offline",this.l);window.addEventListener("online",this.l);this.A||ti(this)}
w(ri,od);function ui(){var a=vi;ri.h||(ri.h=new ri(a));return ri.h}
ri.prototype.dispose=function(){window.removeEventListener("offline",this.l);window.removeEventListener("online",this.l);this.Da.qa(this.A);delete ri.h};
ri.prototype.wa=function(){return this.i};
function ti(a){a.A=a.Da.pa(function(){var b;return A(function(c){if(1==c.h)return a.i?(null==(b=window.navigator)?0:b.onLine)?c.B(3):c.yield(si(a),3):c.yield(si(a),3);ti(a);c.h=0})},3E4)}
function si(a,b){return a.m?a.m:a.m=new Promise(function(c){var d,e,f,g;return A(function(h){switch(h.h){case 1:return d=window.AbortController?new window.AbortController:void 0,f=null==(e=d)?void 0:e.signal,g=!1,Ba(h,2,3),d&&(a.j=a.Da.pa(function(){d.abort()},b||2E4)),h.yield(fetch("/generate_204",{method:"HEAD",
signal:f}),5);case 5:g=!0;case 3:h.S=[h.j];h.l=0;h.m=0;a.m=void 0;a.j&&(a.Da.qa(a.j),a.j=0);g!==a.i&&(a.i=g,a.i?pd(a,"networkstatus-online"):pd(a,"networkstatus-offline"));c(g);Ea(h);break;case 2:Ca(h),g=!1,h.B(3)}})})}
;function wi(){this.data=[];this.h=-1}
wi.prototype.set=function(a,b){b=void 0===b?!0:b;0<=a&&52>a&&Number.isInteger(a)&&this.data[a]!==b&&(this.data[a]=b,this.h=-1)};
wi.prototype.get=function(a){return!!this.data[a]};
function xi(a){-1===a.h&&(a.h=a.data.reduce(function(b,c,d){return b+(c?Math.pow(2,d):0)},0));
return a.h}
;function yi(a,b){this.h=a[C.Symbol.iterator]();this.i=b}
yi.prototype[Symbol.iterator]=function(){return this};
yi.prototype.next=function(){var a=this.h.next();return{value:a.done?void 0:this.i.call(void 0,a.value),done:a.done}};
function zi(a,b){return new yi(a,b)}
;function Ai(){this.blockSize=-1}
;function Bi(){this.blockSize=-1;this.blockSize=64;this.h=[];this.v=[];this.m=[];this.j=[];this.j[0]=128;for(var a=1;a<this.blockSize;++a)this.j[a]=0;this.l=this.i=0;this.reset()}
$a(Bi,Ai);Bi.prototype.reset=function(){this.h[0]=1732584193;this.h[1]=4023233417;this.h[2]=2562383102;this.h[3]=271733878;this.h[4]=3285377520;this.l=this.i=0};
function Ci(a,b,c){c||(c=0);var d=a.m;if("string"===typeof b)for(var e=0;16>e;e++)d[e]=b.charCodeAt(c)<<24|b.charCodeAt(c+1)<<16|b.charCodeAt(c+2)<<8|b.charCodeAt(c+3),c+=4;else for(e=0;16>e;e++)d[e]=b[c]<<24|b[c+1]<<16|b[c+2]<<8|b[c+3],c+=4;for(e=16;80>e;e++){var f=d[e-3]^d[e-8]^d[e-14]^d[e-16];d[e]=(f<<1|f>>>31)&4294967295}b=a.h[0];c=a.h[1];var g=a.h[2],h=a.h[3],k=a.h[4];for(e=0;80>e;e++){if(40>e)if(20>e){f=h^c&(g^h);var l=1518500249}else f=c^g^h,l=1859775393;else 60>e?(f=c&g|h&(c|g),l=2400959708):
(f=c^g^h,l=3395469782);f=(b<<5|b>>>27)+f+k+l+d[e]&4294967295;k=h;h=g;g=(c<<30|c>>>2)&4294967295;c=b;b=f}a.h[0]=a.h[0]+b&4294967295;a.h[1]=a.h[1]+c&4294967295;a.h[2]=a.h[2]+g&4294967295;a.h[3]=a.h[3]+h&4294967295;a.h[4]=a.h[4]+k&4294967295}
Bi.prototype.update=function(a,b){if(null!=a){void 0===b&&(b=a.length);for(var c=b-this.blockSize,d=0,e=this.v,f=this.i;d<b;){if(0==f)for(;d<=c;)Ci(this,a,d),d+=this.blockSize;if("string"===typeof a)for(;d<b;){if(e[f]=a.charCodeAt(d),++f,++d,f==this.blockSize){Ci(this,e);f=0;break}}else for(;d<b;)if(e[f]=a[d],++f,++d,f==this.blockSize){Ci(this,e);f=0;break}}this.i=f;this.l+=b}};
Bi.prototype.digest=function(){var a=[],b=8*this.l;56>this.i?this.update(this.j,56-this.i):this.update(this.j,this.blockSize-(this.i-56));for(var c=this.blockSize-1;56<=c;c--)this.v[c]=b&255,b/=256;Ci(this,this.v);for(c=b=0;5>c;c++)for(var d=24;0<=d;d-=8)a[b]=this.h[c]>>d&255,++b;return a};function Di(a){return"string"==typeof a.className?a.className:a.getAttribute&&a.getAttribute("class")||""}
function Ei(a,b){"string"==typeof a.className?a.className=b:a.setAttribute&&a.setAttribute("class",b)}
function Fi(a,b){a.classList?b=a.classList.contains(b):(a=a.classList?a.classList:Di(a).match(/\S+/g)||[],b=0<=fb(a,b));return b}
function Gi(){var a=document.body;a.classList?a.classList.remove("inverted-hdpi"):Fi(a,"inverted-hdpi")&&Ei(a,Array.prototype.filter.call(a.classList?a.classList:Di(a).match(/\S+/g)||[],function(b){return"inverted-hdpi"!=b}).join(" "))}
;function Hi(){}
Hi.prototype.next=function(){return Ii};
var Ii={done:!0,value:void 0};function Ji(a){return{value:a,done:!1}}
Hi.prototype.Fa=function(){return this};function Ki(a){if(a instanceof Li||a instanceof Mi||a instanceof Ni)return a;if("function"==typeof a.next)return new Li(function(){return a});
if("function"==typeof a[Symbol.iterator])return new Li(function(){return a[Symbol.iterator]()});
if("function"==typeof a.Fa)return new Li(function(){return a.Fa()});
throw Error("Not an iterator or iterable.");}
function Li(a){this.i=a}
Li.prototype.Fa=function(){return new Mi(this.i())};
Li.prototype[Symbol.iterator]=function(){return new Ni(this.i())};
Li.prototype.h=function(){return new Ni(this.i())};
function Mi(a){this.i=a}
w(Mi,Hi);Mi.prototype.next=function(){return this.i.next()};
Mi.prototype[Symbol.iterator]=function(){return new Ni(this.i)};
Mi.prototype.h=function(){return new Ni(this.i)};
function Ni(a){Li.call(this,function(){return a});
this.j=a}
w(Ni,Li);Ni.prototype.next=function(){return this.j.next()};function L(a){H.call(this);this.m=1;this.j=[];this.l=0;this.h=[];this.i={};this.A=!!a}
$a(L,H);m=L.prototype;m.subscribe=function(a,b,c){var d=this.i[a];d||(d=this.i[a]=[]);var e=this.m;this.h[e]=a;this.h[e+1]=b;this.h[e+2]=c;this.m=e+3;d.push(e);return e};
m.unsubscribe=function(a,b,c){if(a=this.i[a]){var d=this.h;if(a=a.find(function(e){return d[e+1]==b&&d[e+2]==c}))return this.Ab(a)}return!1};
m.Ab=function(a){var b=this.h[a];if(b){var c=this.i[b];0!=this.l?(this.j.push(a),this.h[a+1]=function(){}):(c&&lb(c,a),delete this.h[a],delete this.h[a+1],delete this.h[a+2])}return!!b};
m.Ya=function(a,b){var c=this.i[a];if(c){for(var d=Array(arguments.length-1),e=1,f=arguments.length;e<f;e++)d[e-1]=arguments[e];if(this.A)for(e=0;e<c.length;e++){var g=c[e];Oi(this.h[g+1],this.h[g+2],d)}else{this.l++;try{for(e=0,f=c.length;e<f&&!this.Z();e++)g=c[e],this.h[g+1].apply(this.h[g+2],d)}finally{if(this.l--,0<this.j.length&&0==this.l)for(;c=this.j.pop();)this.Ab(c)}}return 0!=e}return!1};
function Oi(a,b,c){Hd(function(){a.apply(b,c)})}
m.clear=function(a){if(a){var b=this.i[a];b&&(b.forEach(this.Ab,this),delete this.i[a])}else this.h.length=0,this.i={}};
m.R=function(){L.Aa.R.call(this);this.clear();this.j.length=0};function Pi(a){this.h=a}
Pi.prototype.set=function(a,b){void 0===b?this.h.remove(a):this.h.set(a,(new gh).serialize(b))};
Pi.prototype.get=function(a){try{var b=this.h.get(a)}catch(c){return}if(null!==b)try{return JSON.parse(b)}catch(c){throw"Storage: Invalid value was encountered";}};
Pi.prototype.remove=function(a){this.h.remove(a)};function Qi(a){this.h=a}
$a(Qi,Pi);function Ri(a){this.data=a}
function Si(a){return void 0===a||a instanceof Ri?a:new Ri(a)}
Qi.prototype.set=function(a,b){Qi.Aa.set.call(this,a,Si(b))};
Qi.prototype.i=function(a){a=Qi.Aa.get.call(this,a);if(void 0===a||a instanceof Object)return a;throw"Storage: Invalid value was encountered";};
Qi.prototype.get=function(a){if(a=this.i(a)){if(a=a.data,void 0===a)throw"Storage: Invalid value was encountered";}else a=void 0;return a};function Ti(a){this.h=a}
$a(Ti,Qi);Ti.prototype.set=function(a,b,c){if(b=Si(b)){if(c){if(c<Za()){Ti.prototype.remove.call(this,a);return}b.expiration=c}b.creation=Za()}Ti.Aa.set.call(this,a,b)};
Ti.prototype.i=function(a){var b=Ti.Aa.i.call(this,a);if(b){var c=b.creation,d=b.expiration;if(d&&d<Za()||c&&c>Za())Ti.prototype.remove.call(this,a);else return b}};function Ui(){}
;function Vi(){}
$a(Vi,Ui);Vi.prototype[Symbol.iterator]=function(){return Ki(this.Fa(!0)).h()};
Vi.prototype.clear=function(){var a=Array.from(this);a=v(a);for(var b=a.next();!b.done;b=a.next())this.remove(b.value)};function Wi(a){this.h=a;this.i=null}
$a(Wi,Vi);m=Wi.prototype;m.isAvailable=function(){var a=this.h;if(a)try{a.setItem("__sak","1");a.removeItem("__sak");var b=!0}catch(c){b=c instanceof DOMException&&("QuotaExceededError"===c.name||22===c.code||1014===c.code||"NS_ERROR_DOM_QUOTA_REACHED"===c.name)&&a&&0!==a.length}else b=!1;return this.i=b};
m.set=function(a,b){Xi(this);try{this.h.setItem(a,b)}catch(c){if(0==this.h.length)throw"Storage mechanism: Storage disabled";throw"Storage mechanism: Quota exceeded";}};
m.get=function(a){Xi(this);a=this.h.getItem(a);if("string"!==typeof a&&null!==a)throw"Storage mechanism: Invalid value was encountered";return a};
m.remove=function(a){Xi(this);this.h.removeItem(a)};
m.Fa=function(a){Xi(this);var b=0,c=this.h,d=new Hi;d.next=function(){if(b>=c.length)return Ii;var e=c.key(b++);if(a)return Ji(e);e=c.getItem(e);if("string"!==typeof e)throw"Storage mechanism: Invalid value was encountered";return Ji(e)};
return d};
m.clear=function(){Xi(this);this.h.clear()};
m.key=function(a){Xi(this);return this.h.key(a)};
function Xi(a){if(null==a.h)throw Error("Storage mechanism: Storage unavailable");var b;(null!=(b=a.i)?b:a.isAvailable())||Ad(Error("Storage mechanism: Storage unavailable"))}
;function Yi(){var a=null;try{a=C.localStorage||null}catch(b){}Wi.call(this,a)}
$a(Yi,Wi);function Zi(a,b){this.i={};this.h=[];this.Wa=this.size=0;var c=arguments.length;if(1<c){if(c%2)throw Error("Uneven number of arguments");for(var d=0;d<c;d+=2)this.set(arguments[d],arguments[d+1])}else if(a)if(a instanceof Zi)for(c=a.Ac(),d=0;d<c.length;d++)this.set(c[d],a.get(c[d]));else for(d in a)this.set(d,a[d])}
m=Zi.prototype;m.Ac=function(){$i(this);return this.h.concat()};
m.has=function(a){return aj(this.i,a)};
m.equals=function(a,b){if(this===a)return!0;if(this.size!=a.size)return!1;b=b||bj;$i(this);for(var c,d=0;c=this.h[d];d++)if(!b(this.get(c),a.get(c)))return!1;return!0};
function bj(a,b){return a===b}
m.clear=function(){this.i={};this.Wa=this.size=this.h.length=0};
m.remove=function(a){return this.delete(a)};
m.delete=function(a){return aj(this.i,a)?(delete this.i[a],--this.size,this.Wa++,this.h.length>2*this.size&&$i(this),!0):!1};
function $i(a){if(a.size!=a.h.length){for(var b=0,c=0;b<a.h.length;){var d=a.h[b];aj(a.i,d)&&(a.h[c++]=d);b++}a.h.length=c}if(a.size!=a.h.length){var e={};for(c=b=0;b<a.h.length;)d=a.h[b],aj(e,d)||(a.h[c++]=d,e[d]=1),b++;a.h.length=c}}
m.get=function(a,b){return aj(this.i,a)?this.i[a]:b};
m.set=function(a,b){aj(this.i,a)||(this.size+=1,this.h.push(a),this.Wa++);this.i[a]=b};
m.forEach=function(a,b){for(var c=this.Ac(),d=0;d<c.length;d++){var e=c[d],f=this.get(e);a.call(b,f,e,this)}};
m.clone=function(){return new Zi(this)};
m.keys=function(){return Ki(this.Fa(!0)).h()};
m.values=function(){return Ki(this.Fa(!1)).h()};
m.entries=function(){var a=this;return zi(this.keys(),function(b){return[b,a.get(b)]})};
m.Fa=function(a){$i(this);var b=0,c=this.Wa,d=this,e=new Hi;e.next=function(){if(c!=d.Wa)throw Error("The map has changed since the iterator was created");if(b>=d.h.length)return Ii;var f=d.h[b++];return Ji(a?f:d.i[f])};
return e};
function aj(a,b){return Object.prototype.hasOwnProperty.call(a,b)}
;function cj(a,b){this.i=a;this.h=null;var c;if(c=Ec)c=!(9<=Number(Rc));if(c){dj||(dj=new Zi);this.h=dj.get(a);this.h||(b?this.h=document.getElementById(b):(this.h=document.createElement("userdata"),this.h.addBehavior("#default#userData"),document.body.appendChild(this.h)),dj.set(a,this.h));try{this.h.load(this.i)}catch(d){this.h=null}}}
$a(cj,Vi);var ej={".":".2E","!":".21","~":".7E","*":".2A","'":".27","(":".28",")":".29","%":"."},dj=null;function fj(a){return"_"+encodeURIComponent(a).replace(/[.!~*'()%]/g,function(b){return ej[b]})}
m=cj.prototype;m.isAvailable=function(){return!!this.h};
m.set=function(a,b){this.h.setAttribute(fj(a),b);gj(this)};
m.get=function(a){a=this.h.getAttribute(fj(a));if("string"!==typeof a&&null!==a)throw"Storage mechanism: Invalid value was encountered";return a};
m.remove=function(a){this.h.removeAttribute(fj(a));gj(this)};
m.Fa=function(a){var b=0,c=this.h.XMLDocument.documentElement.attributes,d=new Hi;d.next=function(){if(b>=c.length)return Ii;var e=c[b++];if(a)return Ji(decodeURIComponent(e.nodeName.replace(/\./g,"%")).slice(1));e=e.nodeValue;if("string"!==typeof e)throw"Storage mechanism: Invalid value was encountered";return Ji(e)};
return d};
m.clear=function(){for(var a=this.h.XMLDocument.documentElement,b=a.attributes.length;0<b;b--)a.removeAttribute(a.attributes[b-1].nodeName);gj(this)};
function gj(a){try{a.h.save(a.i)}catch(b){throw"Storage mechanism: Quota exceeded";}}
;function hj(a,b){this.i=a;this.h=b+"::"}
$a(hj,Vi);hj.prototype.set=function(a,b){this.i.set(this.h+a,b)};
hj.prototype.get=function(a){return this.i.get(this.h+a)};
hj.prototype.remove=function(a){this.i.remove(this.h+a)};
hj.prototype.Fa=function(a){var b=this.i[Symbol.iterator](),c=this,d=new Hi;d.next=function(){var e=b.next();if(e.done)return e;for(e=e.value;e.slice(0,c.h.length)!=c.h;){e=b.next();if(e.done)return e;e=e.value}return Ji(a?e.slice(c.h.length):c.i.get(e))};
return d};/*

 (The MIT License)

 Copyright (C) 2014 by Vitaly Puzrin

 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in
 all copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 THE SOFTWARE.

 -----------------------------------------------------------------------------
 Ported from zlib, which is under the following license
 https://github.com/madler/zlib/blob/master/zlib.h

 zlib.h -- interface of the 'zlib' general purpose compression library
   version 1.2.8, April 28th, 2013
   Copyright (C) 1995-2013 Jean-loup Gailly and Mark Adler
   This software is provided 'as-is', without any express or implied
   warranty.  In no event will the authors be held liable for any damages
   arising from the use of this software.
   Permission is granted to anyone to use this software for any purpose,
   including commercial applications, and to alter it and redistribute it
   freely, subject to the following restrictions:
   1. The origin of this software must not be misrepresented; you must not
      claim that you wrote the original software. If you use this software
      in a product, an acknowledgment in the product documentation would be
      appreciated but is not required.
   2. Altered source versions must be plainly marked as such, and must not be
      misrepresented as being the original software.
   3. This notice may not be removed or altered from any source distribution.
   Jean-loup Gailly        Mark Adler
   jloup@gzip.org          madler@alumni.caltech.edu
   The data format used by the zlib library is described by RFCs (Request for
   Comments) 1950 to 1952 in the files http://tools.ietf.org/html/rfc1950
   (zlib format), rfc1951 (deflate format) and rfc1952 (gzip format).
*/
var N={},ij="undefined"!==typeof Uint8Array&&"undefined"!==typeof Uint16Array&&"undefined"!==typeof Int32Array;N.assign=function(a){for(var b=Array.prototype.slice.call(arguments,1);b.length;){var c=b.shift();if(c){if("object"!==typeof c)throw new TypeError(c+"must be non-object");for(var d in c)Object.prototype.hasOwnProperty.call(c,d)&&(a[d]=c[d])}}return a};
N.Rc=function(a,b){if(a.length===b)return a;if(a.subarray)return a.subarray(0,b);a.length=b;return a};
var jj={mb:function(a,b,c,d,e){if(b.subarray&&a.subarray)a.set(b.subarray(c,c+d),e);else for(var f=0;f<d;f++)a[e+f]=b[c+f]},
hd:function(a){var b,c;var d=c=0;for(b=a.length;d<b;d++)c+=a[d].length;var e=new Uint8Array(c);d=c=0;for(b=a.length;d<b;d++){var f=a[d];e.set(f,c);c+=f.length}return e}},kj={mb:function(a,b,c,d,e){for(var f=0;f<d;f++)a[e+f]=b[c+f]},
hd:function(a){return[].concat.apply([],a)}};
N.Ye=function(){ij?(N.lb=Uint8Array,N.Ha=Uint16Array,N.Nd=Int32Array,N.assign(N,jj)):(N.lb=Array,N.Ha=Array,N.Nd=Array,N.assign(N,kj))};
N.Ye();var lj=!0;try{new Uint8Array(1)}catch(a){lj=!1}
function mj(a){var b,c,d=a.length,e=0;for(b=0;b<d;b++){var f=a.charCodeAt(b);if(55296===(f&64512)&&b+1<d){var g=a.charCodeAt(b+1);56320===(g&64512)&&(f=65536+(f-55296<<10)+(g-56320),b++)}e+=128>f?1:2048>f?2:65536>f?3:4}var h=new N.lb(e);for(b=c=0;c<e;b++)f=a.charCodeAt(b),55296===(f&64512)&&b+1<d&&(g=a.charCodeAt(b+1),56320===(g&64512)&&(f=65536+(f-55296<<10)+(g-56320),b++)),128>f?h[c++]=f:(2048>f?h[c++]=192|f>>>6:(65536>f?h[c++]=224|f>>>12:(h[c++]=240|f>>>18,h[c++]=128|f>>>12&63),h[c++]=128|f>>>
6&63),h[c++]=128|f&63);return h}
;var nj={};nj=function(a,b,c,d){var e=a&65535|0;a=a>>>16&65535|0;for(var f;0!==c;){f=2E3<c?2E3:c;c-=f;do e=e+b[d++]|0,a=a+e|0;while(--f);e%=65521;a%=65521}return e|a<<16|0};for(var oj={},pj,qj=[],rj=0;256>rj;rj++){pj=rj;for(var sj=0;8>sj;sj++)pj=pj&1?3988292384^pj>>>1:pj>>>1;qj[rj]=pj}oj=function(a,b,c,d){c=d+c;for(a^=-1;d<c;d++)a=a>>>8^qj[(a^b[d])&255];return a^-1};var tj={};tj={2:"need dictionary",1:"stream end",0:"","-1":"file error","-2":"stream error","-3":"data error","-4":"insufficient memory","-5":"buffer error","-6":"incompatible version"};function uj(a){for(var b=a.length;0<=--b;)a[b]=0}
var vj=[0,0,0,0,0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,0],wj=[0,0,0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13],xj=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,3,7],yj=[16,17,18,0,8,7,9,6,10,5,11,4,12,3,13,2,14,1,15],zj=Array(576);uj(zj);var Aj=Array(60);uj(Aj);var Bj=Array(512);uj(Bj);var Cj=Array(256);uj(Cj);var Dj=Array(29);uj(Dj);var Ej=Array(30);uj(Ej);function Fj(a,b,c,d,e){this.Fd=a;this.de=b;this.ce=c;this.Xd=d;this.ze=e;this.ld=a&&a.length}
var Gj,Hj,Ij;function Jj(a,b){this.gd=a;this.vb=0;this.Va=b}
function Kj(a,b){a.W[a.pending++]=b&255;a.W[a.pending++]=b>>>8&255}
function Lj(a,b,c){a.fa>16-c?(a.ma|=b<<a.fa&65535,Kj(a,a.ma),a.ma=b>>16-a.fa,a.fa+=c-16):(a.ma|=b<<a.fa&65535,a.fa+=c)}
function Mj(a,b,c){Lj(a,c[2*b],c[2*b+1])}
function Nj(a,b){var c=0;do c|=a&1,a>>>=1,c<<=1;while(0<--b);return c>>>1}
function Oj(a,b,c){var d=Array(16),e=0,f;for(f=1;15>=f;f++)d[f]=e=e+c[f-1]<<1;for(c=0;c<=b;c++)e=a[2*c+1],0!==e&&(a[2*c]=Nj(d[e]++,e))}
function Pj(a){var b;for(b=0;286>b;b++)a.ra[2*b]=0;for(b=0;30>b;b++)a.bb[2*b]=0;for(b=0;19>b;b++)a.ia[2*b]=0;a.ra[512]=1;a.Na=a.zb=0;a.ya=a.matches=0}
function Qj(a){8<a.fa?Kj(a,a.ma):0<a.fa&&(a.W[a.pending++]=a.ma);a.ma=0;a.fa=0}
function Rj(a,b,c){Qj(a);Kj(a,c);Kj(a,~c);N.mb(a.W,a.window,b,c,a.pending);a.pending+=c}
function Sj(a,b,c,d){var e=2*b,f=2*c;return a[e]<a[f]||a[e]===a[f]&&d[b]<=d[c]}
function Tj(a,b,c){for(var d=a.X[c],e=c<<1;e<=a.La;){e<a.La&&Sj(b,a.X[e+1],a.X[e],a.depth)&&e++;if(Sj(b,d,a.X[e],a.depth))break;a.X[c]=a.X[e];c=e;e<<=1}a.X[c]=d}
function Uj(a,b,c){var d=0;if(0!==a.ya){do{var e=a.W[a.Db+2*d]<<8|a.W[a.Db+2*d+1];var f=a.W[a.Fc+d];d++;if(0===e)Mj(a,f,b);else{var g=Cj[f];Mj(a,g+256+1,b);var h=vj[g];0!==h&&(f-=Dj[g],Lj(a,f,h));e--;g=256>e?Bj[e]:Bj[256+(e>>>7)];Mj(a,g,c);h=wj[g];0!==h&&(e-=Ej[g],Lj(a,e,h))}}while(d<a.ya)}Mj(a,256,b)}
function Vj(a,b){var c=b.gd,d=b.Va.Fd,e=b.Va.ld,f=b.Va.Xd,g,h=-1;a.La=0;a.qb=573;for(g=0;g<f;g++)0!==c[2*g]?(a.X[++a.La]=h=g,a.depth[g]=0):c[2*g+1]=0;for(;2>a.La;){var k=a.X[++a.La]=2>h?++h:0;c[2*k]=1;a.depth[k]=0;a.Na--;e&&(a.zb-=d[2*k+1])}b.vb=h;for(g=a.La>>1;1<=g;g--)Tj(a,c,g);k=f;do g=a.X[1],a.X[1]=a.X[a.La--],Tj(a,c,1),d=a.X[1],a.X[--a.qb]=g,a.X[--a.qb]=d,c[2*k]=c[2*g]+c[2*d],a.depth[k]=(a.depth[g]>=a.depth[d]?a.depth[g]:a.depth[d])+1,c[2*g+1]=c[2*d+1]=k,a.X[1]=k++,Tj(a,c,1);while(2<=a.La);a.X[--a.qb]=
a.X[1];g=b.gd;k=b.vb;d=b.Va.Fd;e=b.Va.ld;f=b.Va.de;var l=b.Va.ce,n=b.Va.ze,p,r=0;for(p=0;15>=p;p++)a.Ia[p]=0;g[2*a.X[a.qb]+1]=0;for(b=a.qb+1;573>b;b++){var t=a.X[b];p=g[2*g[2*t+1]+1]+1;p>n&&(p=n,r++);g[2*t+1]=p;if(!(t>k)){a.Ia[p]++;var x=0;t>=l&&(x=f[t-l]);var z=g[2*t];a.Na+=z*(p+x);e&&(a.zb+=z*(d[2*t+1]+x))}}if(0!==r){do{for(p=n-1;0===a.Ia[p];)p--;a.Ia[p]--;a.Ia[p+1]+=2;a.Ia[n]--;r-=2}while(0<r);for(p=n;0!==p;p--)for(t=a.Ia[p];0!==t;)d=a.X[--b],d>k||(g[2*d+1]!==p&&(a.Na+=(p-g[2*d+1])*g[2*d],g[2*
d+1]=p),t--)}Oj(c,h,a.Ia)}
function Wj(a,b,c){var d,e=-1,f=b[1],g=0,h=7,k=4;0===f&&(h=138,k=3);b[2*(c+1)+1]=65535;for(d=0;d<=c;d++){var l=f;f=b[2*(d+1)+1];++g<h&&l===f||(g<k?a.ia[2*l]+=g:0!==l?(l!==e&&a.ia[2*l]++,a.ia[32]++):10>=g?a.ia[34]++:a.ia[36]++,g=0,e=l,0===f?(h=138,k=3):l===f?(h=6,k=3):(h=7,k=4))}}
function Xj(a,b,c){var d,e=-1,f=b[1],g=0,h=7,k=4;0===f&&(h=138,k=3);for(d=0;d<=c;d++){var l=f;f=b[2*(d+1)+1];if(!(++g<h&&l===f)){if(g<k){do Mj(a,l,a.ia);while(0!==--g)}else 0!==l?(l!==e&&(Mj(a,l,a.ia),g--),Mj(a,16,a.ia),Lj(a,g-3,2)):10>=g?(Mj(a,17,a.ia),Lj(a,g-3,3)):(Mj(a,18,a.ia),Lj(a,g-11,7));g=0;e=l;0===f?(h=138,k=3):l===f?(h=6,k=3):(h=7,k=4)}}}
function Yj(a){var b=4093624447,c;for(c=0;31>=c;c++,b>>>=1)if(b&1&&0!==a.ra[2*c])return 0;if(0!==a.ra[18]||0!==a.ra[20]||0!==a.ra[26])return 1;for(c=32;256>c;c++)if(0!==a.ra[2*c])return 1;return 0}
var Zj=!1;function ak(a,b,c){a.W[a.Db+2*a.ya]=b>>>8&255;a.W[a.Db+2*a.ya+1]=b&255;a.W[a.Fc+a.ya]=c&255;a.ya++;0===b?a.ra[2*c]++:(a.matches++,b--,a.ra[2*(Cj[c]+256+1)]++,a.bb[2*(256>b?Bj[b]:Bj[256+(b>>>7)])]++);return a.ya===a.Ib-1}
;function bk(a,b){a.msg=tj[b];return b}
function ck(a){for(var b=a.length;0<=--b;)a[b]=0}
function dk(a){var b=a.state,c=b.pending;c>a.M&&(c=a.M);0!==c&&(N.mb(a.output,b.W,b.Lb,c,a.wb),a.wb+=c,b.Lb+=c,a.Sc+=c,a.M-=c,b.pending-=c,0===b.pending&&(b.Lb=0))}
function ek(a,b){var c=0<=a.va?a.va:-1,d=a.o-a.va,e=0;if(0<a.level){2===a.I.uc&&(a.I.uc=Yj(a));Vj(a,a.dc);Vj(a,a.Yb);Wj(a,a.ra,a.dc.vb);Wj(a,a.bb,a.Yb.vb);Vj(a,a.Yc);for(e=18;3<=e&&0===a.ia[2*yj[e]+1];e--);a.Na+=3*(e+1)+14;var f=a.Na+3+7>>>3;var g=a.zb+3+7>>>3;g<=f&&(f=g)}else f=g=d+5;if(d+4<=f&&-1!==c)Lj(a,b?1:0,3),Rj(a,c,d);else if(4===a.strategy||g===f)Lj(a,2+(b?1:0),3),Uj(a,zj,Aj);else{Lj(a,4+(b?1:0),3);c=a.dc.vb+1;d=a.Yb.vb+1;e+=1;Lj(a,c-257,5);Lj(a,d-1,5);Lj(a,e-4,4);for(f=0;f<e;f++)Lj(a,a.ia[2*
yj[f]+1],3);Xj(a,a.ra,c-1);Xj(a,a.bb,d-1);Uj(a,a.ra,a.bb)}Pj(a);b&&Qj(a);a.va=a.o;dk(a.I)}
function O(a,b){a.W[a.pending++]=b}
function fk(a,b){a.W[a.pending++]=b>>>8&255;a.W[a.pending++]=b&255}
function gk(a,b){var c=a.pd,d=a.o,e=a.xa,f=a.qd,g=a.o>a.ka-262?a.o-(a.ka-262):0,h=a.window,k=a.Xa,l=a.Ga,n=a.o+258,p=h[d+e-1],r=h[d+e];a.xa>=a.kd&&(c>>=2);f>a.u&&(f=a.u);do{var t=b;if(h[t+e]===r&&h[t+e-1]===p&&h[t]===h[d]&&h[++t]===h[d+1]){d+=2;for(t++;h[++d]===h[++t]&&h[++d]===h[++t]&&h[++d]===h[++t]&&h[++d]===h[++t]&&h[++d]===h[++t]&&h[++d]===h[++t]&&h[++d]===h[++t]&&h[++d]===h[++t]&&d<n;);t=258-(n-d);d=n-258;if(t>e){a.ub=b;e=t;if(t>=f)break;p=h[d+e-1];r=h[d+e]}}}while((b=l[b&k])>g&&0!==--c);return e<=
a.u?e:a.u}
function hk(a){var b=a.ka,c;do{var d=a.Ld-a.u-a.o;if(a.o>=b+(b-262)){N.mb(a.window,a.window,b,b,0);a.ub-=b;a.o-=b;a.va-=b;var e=c=a.cc;do{var f=a.head[--e];a.head[e]=f>=b?f-b:0}while(--c);e=c=b;do f=a.Ga[--e],a.Ga[e]=f>=b?f-b:0;while(--c);d+=b}if(0===a.I.la)break;e=a.I;c=a.window;f=a.o+a.u;var g=e.la;g>d&&(g=d);0===g?c=0:(e.la-=g,N.mb(c,e.input,e.hb,g,f),1===e.state.wrap?e.H=nj(e.H,c,g,f):2===e.state.wrap&&(e.H=oj(e.H,c,g,f)),e.hb+=g,e.kb+=g,c=g);a.u+=c;if(3<=a.u+a.sa)for(d=a.o-a.sa,a.K=a.window[d],
a.K=(a.K<<a.Ka^a.window[d+1])&a.Ja;a.sa&&!(a.K=(a.K<<a.Ka^a.window[d+3-1])&a.Ja,a.Ga[d&a.Xa]=a.head[a.K],a.head[a.K]=d,d++,a.sa--,3>a.u+a.sa););}while(262>a.u&&0!==a.I.la)}
function ik(a,b){for(var c;;){if(262>a.u){hk(a);if(262>a.u&&0===b)return 1;if(0===a.u)break}c=0;3<=a.u&&(a.K=(a.K<<a.Ka^a.window[a.o+3-1])&a.Ja,c=a.Ga[a.o&a.Xa]=a.head[a.K],a.head[a.K]=a.o);0!==c&&a.o-c<=a.ka-262&&(a.P=gk(a,c));if(3<=a.P)if(c=ak(a,a.o-a.ub,a.P-3),a.u-=a.P,a.P<=a.Hc&&3<=a.u){a.P--;do a.o++,a.K=(a.K<<a.Ka^a.window[a.o+3-1])&a.Ja,a.Ga[a.o&a.Xa]=a.head[a.K],a.head[a.K]=a.o;while(0!==--a.P);a.o++}else a.o+=a.P,a.P=0,a.K=a.window[a.o],a.K=(a.K<<a.Ka^a.window[a.o+1])&a.Ja;else c=ak(a,0,
a.window[a.o]),a.u--,a.o++;if(c&&(ek(a,!1),0===a.I.M))return 1}a.sa=2>a.o?a.o:2;return 4===b?(ek(a,!0),0===a.I.M?3:4):a.ya&&(ek(a,!1),0===a.I.M)?1:2}
function jk(a,b){for(var c,d;;){if(262>a.u){hk(a);if(262>a.u&&0===b)return 1;if(0===a.u)break}c=0;3<=a.u&&(a.K=(a.K<<a.Ka^a.window[a.o+3-1])&a.Ja,c=a.Ga[a.o&a.Xa]=a.head[a.K],a.head[a.K]=a.o);a.xa=a.P;a.td=a.ub;a.P=2;0!==c&&a.xa<a.Hc&&a.o-c<=a.ka-262&&(a.P=gk(a,c),5>=a.P&&(1===a.strategy||3===a.P&&4096<a.o-a.ub)&&(a.P=2));if(3<=a.xa&&a.P<=a.xa){d=a.o+a.u-3;c=ak(a,a.o-1-a.td,a.xa-3);a.u-=a.xa-1;a.xa-=2;do++a.o<=d&&(a.K=(a.K<<a.Ka^a.window[a.o+3-1])&a.Ja,a.Ga[a.o&a.Xa]=a.head[a.K],a.head[a.K]=a.o);
while(0!==--a.xa);a.fb=0;a.P=2;a.o++;if(c&&(ek(a,!1),0===a.I.M))return 1}else if(a.fb){if((c=ak(a,0,a.window[a.o-1]))&&ek(a,!1),a.o++,a.u--,0===a.I.M)return 1}else a.fb=1,a.o++,a.u--}a.fb&&(ak(a,0,a.window[a.o-1]),a.fb=0);a.sa=2>a.o?a.o:2;return 4===b?(ek(a,!0),0===a.I.M?3:4):a.ya&&(ek(a,!1),0===a.I.M)?1:2}
function kk(a,b){for(var c,d,e,f=a.window;;){if(258>=a.u){hk(a);if(258>=a.u&&0===b)return 1;if(0===a.u)break}a.P=0;if(3<=a.u&&0<a.o&&(d=a.o-1,c=f[d],c===f[++d]&&c===f[++d]&&c===f[++d])){for(e=a.o+258;c===f[++d]&&c===f[++d]&&c===f[++d]&&c===f[++d]&&c===f[++d]&&c===f[++d]&&c===f[++d]&&c===f[++d]&&d<e;);a.P=258-(e-d);a.P>a.u&&(a.P=a.u)}3<=a.P?(c=ak(a,1,a.P-3),a.u-=a.P,a.o+=a.P,a.P=0):(c=ak(a,0,a.window[a.o]),a.u--,a.o++);if(c&&(ek(a,!1),0===a.I.M))return 1}a.sa=0;return 4===b?(ek(a,!0),0===a.I.M?3:4):
a.ya&&(ek(a,!1),0===a.I.M)?1:2}
function lk(a,b){for(var c;;){if(0===a.u&&(hk(a),0===a.u)){if(0===b)return 1;break}a.P=0;c=ak(a,0,a.window[a.o]);a.u--;a.o++;if(c&&(ek(a,!1),0===a.I.M))return 1}a.sa=0;return 4===b?(ek(a,!0),0===a.I.M?3:4):a.ya&&(ek(a,!1),0===a.I.M)?1:2}
function mk(a,b,c,d,e){this.le=a;this.ye=b;this.Be=c;this.xe=d;this.ge=e}
var nk;nk=[new mk(0,0,0,0,function(a,b){var c=65535;for(c>a.za-5&&(c=a.za-5);;){if(1>=a.u){hk(a);if(0===a.u&&0===b)return 1;if(0===a.u)break}a.o+=a.u;a.u=0;var d=a.va+c;if(0===a.o||a.o>=d)if(a.u=a.o-d,a.o=d,ek(a,!1),0===a.I.M)return 1;if(a.o-a.va>=a.ka-262&&(ek(a,!1),0===a.I.M))return 1}a.sa=0;if(4===b)return ek(a,!0),0===a.I.M?3:4;a.o>a.va&&ek(a,!1);return 1}),
new mk(4,4,8,4,ik),new mk(4,5,16,8,ik),new mk(4,6,32,32,ik),new mk(4,4,16,16,jk),new mk(8,16,32,32,jk),new mk(8,16,128,128,jk),new mk(8,32,128,256,jk),new mk(32,128,258,1024,jk),new mk(32,258,258,4096,jk)];
function ok(){this.I=null;this.status=0;this.W=null;this.wrap=this.pending=this.Lb=this.za=0;this.G=null;this.Ca=0;this.method=8;this.sb=-1;this.Xa=this.Uc=this.ka=0;this.window=null;this.Ld=0;this.head=this.Ga=null;this.qd=this.kd=this.strategy=this.level=this.Hc=this.pd=this.xa=this.u=this.ub=this.o=this.fb=this.td=this.P=this.va=this.Ka=this.Ja=this.Cc=this.cc=this.K=0;this.ra=new N.Ha(1146);this.bb=new N.Ha(122);this.ia=new N.Ha(78);ck(this.ra);ck(this.bb);ck(this.ia);this.Yc=this.Yb=this.dc=
null;this.Ia=new N.Ha(16);this.X=new N.Ha(573);ck(this.X);this.qb=this.La=0;this.depth=new N.Ha(573);ck(this.depth);this.fa=this.ma=this.sa=this.matches=this.zb=this.Na=this.Db=this.ya=this.Ib=this.Fc=0}
function pk(a,b){if(!a||!a.state||5<b||0>b)return a?bk(a,-2):-2;var c=a.state;if(!a.output||!a.input&&0!==a.la||666===c.status&&4!==b)return bk(a,0===a.M?-5:-2);c.I=a;var d=c.sb;c.sb=b;if(42===c.status)if(2===c.wrap)a.H=0,O(c,31),O(c,139),O(c,8),c.G?(O(c,(c.G.text?1:0)+(c.G.Ra?2:0)+(c.G.extra?4:0)+(c.G.name?8:0)+(c.G.comment?16:0)),O(c,c.G.time&255),O(c,c.G.time>>8&255),O(c,c.G.time>>16&255),O(c,c.G.time>>24&255),O(c,9===c.level?2:2<=c.strategy||2>c.level?4:0),O(c,c.G.os&255),c.G.extra&&c.G.extra.length&&
(O(c,c.G.extra.length&255),O(c,c.G.extra.length>>8&255)),c.G.Ra&&(a.H=oj(a.H,c.W,c.pending,0)),c.Ca=0,c.status=69):(O(c,0),O(c,0),O(c,0),O(c,0),O(c,0),O(c,9===c.level?2:2<=c.strategy||2>c.level?4:0),O(c,3),c.status=113);else{var e=8+(c.Uc-8<<4)<<8;e|=(2<=c.strategy||2>c.level?0:6>c.level?1:6===c.level?2:3)<<6;0!==c.o&&(e|=32);c.status=113;fk(c,e+(31-e%31));0!==c.o&&(fk(c,a.H>>>16),fk(c,a.H&65535));a.H=1}if(69===c.status)if(c.G.extra){for(e=c.pending;c.Ca<(c.G.extra.length&65535)&&(c.pending!==c.za||
(c.G.Ra&&c.pending>e&&(a.H=oj(a.H,c.W,c.pending-e,e)),dk(a),e=c.pending,c.pending!==c.za));)O(c,c.G.extra[c.Ca]&255),c.Ca++;c.G.Ra&&c.pending>e&&(a.H=oj(a.H,c.W,c.pending-e,e));c.Ca===c.G.extra.length&&(c.Ca=0,c.status=73)}else c.status=73;if(73===c.status)if(c.G.name){e=c.pending;do{if(c.pending===c.za&&(c.G.Ra&&c.pending>e&&(a.H=oj(a.H,c.W,c.pending-e,e)),dk(a),e=c.pending,c.pending===c.za)){var f=1;break}f=c.Ca<c.G.name.length?c.G.name.charCodeAt(c.Ca++)&255:0;O(c,f)}while(0!==f);c.G.Ra&&c.pending>
e&&(a.H=oj(a.H,c.W,c.pending-e,e));0===f&&(c.Ca=0,c.status=91)}else c.status=91;if(91===c.status)if(c.G.comment){e=c.pending;do{if(c.pending===c.za&&(c.G.Ra&&c.pending>e&&(a.H=oj(a.H,c.W,c.pending-e,e)),dk(a),e=c.pending,c.pending===c.za)){f=1;break}f=c.Ca<c.G.comment.length?c.G.comment.charCodeAt(c.Ca++)&255:0;O(c,f)}while(0!==f);c.G.Ra&&c.pending>e&&(a.H=oj(a.H,c.W,c.pending-e,e));0===f&&(c.status=103)}else c.status=103;103===c.status&&(c.G.Ra?(c.pending+2>c.za&&dk(a),c.pending+2<=c.za&&(O(c,a.H&
255),O(c,a.H>>8&255),a.H=0,c.status=113)):c.status=113);if(0!==c.pending){if(dk(a),0===a.M)return c.sb=-1,0}else if(0===a.la&&(b<<1)-(4<b?9:0)<=(d<<1)-(4<d?9:0)&&4!==b)return bk(a,-5);if(666===c.status&&0!==a.la)return bk(a,-5);if(0!==a.la||0!==c.u||0!==b&&666!==c.status){d=2===c.strategy?lk(c,b):3===c.strategy?kk(c,b):nk[c.level].ge(c,b);if(3===d||4===d)c.status=666;if(1===d||3===d)return 0===a.M&&(c.sb=-1),0;if(2===d&&(1===b?(Lj(c,2,3),Mj(c,256,zj),16===c.fa?(Kj(c,c.ma),c.ma=0,c.fa=0):8<=c.fa&&
(c.W[c.pending++]=c.ma&255,c.ma>>=8,c.fa-=8)):5!==b&&(Lj(c,0,3),Rj(c,0,0),3===b&&(ck(c.head),0===c.u&&(c.o=0,c.va=0,c.sa=0))),dk(a),0===a.M))return c.sb=-1,0}if(4!==b)return 0;if(0>=c.wrap)return 1;2===c.wrap?(O(c,a.H&255),O(c,a.H>>8&255),O(c,a.H>>16&255),O(c,a.H>>24&255),O(c,a.kb&255),O(c,a.kb>>8&255),O(c,a.kb>>16&255),O(c,a.kb>>24&255)):(fk(c,a.H>>>16),fk(c,a.H&65535));dk(a);0<c.wrap&&(c.wrap=-c.wrap);return 0!==c.pending?0:1}
;var qk={};qk=function(){this.input=null;this.kb=this.la=this.hb=0;this.output=null;this.Sc=this.M=this.wb=0;this.msg="";this.state=null;this.uc=2;this.H=0};var rk=Object.prototype.toString;
function sk(a){if(!(this instanceof sk))return new sk(a);a=this.options=N.assign({level:-1,method:8,chunkSize:16384,windowBits:15,memLevel:8,strategy:0,to:""},a||{});a.raw&&0<a.windowBits?a.windowBits=-a.windowBits:a.gzip&&0<a.windowBits&&16>a.windowBits&&(a.windowBits+=16);this.err=0;this.msg="";this.ended=!1;this.chunks=[];this.I=new qk;this.I.M=0;var b=this.I;var c=a.level,d=a.method,e=a.windowBits,f=a.memLevel,g=a.strategy;if(b){var h=1;-1===c&&(c=6);0>e?(h=0,e=-e):15<e&&(h=2,e-=16);if(1>f||9<
f||8!==d||8>e||15<e||0>c||9<c||0>g||4<g)b=bk(b,-2);else{8===e&&(e=9);var k=new ok;b.state=k;k.I=b;k.wrap=h;k.G=null;k.Uc=e;k.ka=1<<k.Uc;k.Xa=k.ka-1;k.Cc=f+7;k.cc=1<<k.Cc;k.Ja=k.cc-1;k.Ka=~~((k.Cc+3-1)/3);k.window=new N.lb(2*k.ka);k.head=new N.Ha(k.cc);k.Ga=new N.Ha(k.ka);k.Ib=1<<f+6;k.za=4*k.Ib;k.W=new N.lb(k.za);k.Db=1*k.Ib;k.Fc=3*k.Ib;k.level=c;k.strategy=g;k.method=d;if(b&&b.state){b.kb=b.Sc=0;b.uc=2;c=b.state;c.pending=0;c.Lb=0;0>c.wrap&&(c.wrap=-c.wrap);c.status=c.wrap?42:113;b.H=2===c.wrap?
0:1;c.sb=0;if(!Zj){d=Array(16);for(f=g=0;28>f;f++)for(Dj[f]=g,e=0;e<1<<vj[f];e++)Cj[g++]=f;Cj[g-1]=f;for(f=g=0;16>f;f++)for(Ej[f]=g,e=0;e<1<<wj[f];e++)Bj[g++]=f;for(g>>=7;30>f;f++)for(Ej[f]=g<<7,e=0;e<1<<wj[f]-7;e++)Bj[256+g++]=f;for(e=0;15>=e;e++)d[e]=0;for(e=0;143>=e;)zj[2*e+1]=8,e++,d[8]++;for(;255>=e;)zj[2*e+1]=9,e++,d[9]++;for(;279>=e;)zj[2*e+1]=7,e++,d[7]++;for(;287>=e;)zj[2*e+1]=8,e++,d[8]++;Oj(zj,287,d);for(e=0;30>e;e++)Aj[2*e+1]=5,Aj[2*e]=Nj(e,5);Gj=new Fj(zj,vj,257,286,15);Hj=new Fj(Aj,
wj,0,30,15);Ij=new Fj([],xj,0,19,7);Zj=!0}c.dc=new Jj(c.ra,Gj);c.Yb=new Jj(c.bb,Hj);c.Yc=new Jj(c.ia,Ij);c.ma=0;c.fa=0;Pj(c);c=0}else c=bk(b,-2);0===c&&(b=b.state,b.Ld=2*b.ka,ck(b.head),b.Hc=nk[b.level].ye,b.kd=nk[b.level].le,b.qd=nk[b.level].Be,b.pd=nk[b.level].xe,b.o=0,b.va=0,b.u=0,b.sa=0,b.P=b.xa=2,b.fb=0,b.K=0);b=c}}else b=-2;if(0!==b)throw Error(tj[b]);a.header&&(b=this.I)&&b.state&&2===b.state.wrap&&(b.state.G=a.header);if(a.dictionary){var l;"string"===typeof a.dictionary?l=mj(a.dictionary):
"[object ArrayBuffer]"===rk.call(a.dictionary)?l=new Uint8Array(a.dictionary):l=a.dictionary;a=this.I;f=l;g=f.length;if(a&&a.state)if(l=a.state,b=l.wrap,2===b||1===b&&42!==l.status||l.u)b=-2;else{1===b&&(a.H=nj(a.H,f,g,0));l.wrap=0;g>=l.ka&&(0===b&&(ck(l.head),l.o=0,l.va=0,l.sa=0),c=new N.lb(l.ka),N.mb(c,f,g-l.ka,l.ka,0),f=c,g=l.ka);c=a.la;d=a.hb;e=a.input;a.la=g;a.hb=0;a.input=f;for(hk(l);3<=l.u;){f=l.o;g=l.u-2;do l.K=(l.K<<l.Ka^l.window[f+3-1])&l.Ja,l.Ga[f&l.Xa]=l.head[l.K],l.head[l.K]=f,f++;while(--g);
l.o=f;l.u=2;hk(l)}l.o+=l.u;l.va=l.o;l.sa=l.u;l.u=0;l.P=l.xa=2;l.fb=0;a.hb=d;a.input=e;a.la=c;l.wrap=b;b=0}else b=-2;if(0!==b)throw Error(tj[b]);this.Rf=!0}}
sk.prototype.push=function(a,b){var c=this.I,d=this.options.chunkSize;if(this.ended)return!1;var e=b===~~b?b:!0===b?4:0;"string"===typeof a?c.input=mj(a):"[object ArrayBuffer]"===rk.call(a)?c.input=new Uint8Array(a):c.input=a;c.hb=0;c.la=c.input.length;do{0===c.M&&(c.output=new N.lb(d),c.wb=0,c.M=d);a=pk(c,e);if(1!==a&&0!==a)return tk(this,a),this.ended=!0,!1;if(0===c.M||0===c.la&&(4===e||2===e))if("string"===this.options.to){var f=N.Rc(c.output,c.wb);b=f;f=f.length;if(65537>f&&(b.subarray&&lj||!b.subarray))b=
String.fromCharCode.apply(null,N.Rc(b,f));else{for(var g="",h=0;h<f;h++)g+=String.fromCharCode(b[h]);b=g}this.chunks.push(b)}else b=N.Rc(c.output,c.wb),this.chunks.push(b)}while((0<c.la||0===c.M)&&1!==a);if(4===e)return(c=this.I)&&c.state?(d=c.state.status,42!==d&&69!==d&&73!==d&&91!==d&&103!==d&&113!==d&&666!==d?a=bk(c,-2):(c.state=null,a=113===d?bk(c,-3):0)):a=-2,tk(this,a),this.ended=!0,0===a;2===e&&(tk(this,0),c.M=0);return!0};
function tk(a,b){0===b&&(a.result="string"===a.options.to?a.chunks.join(""):N.hd(a.chunks));a.chunks=[];a.err=b;a.msg=a.I.msg}
function uk(a,b){b=b||{};b.gzip=!0;b=new sk(b);b.push(a,!0);if(b.err)throw b.msg||tj[b.err];return b.result}
;function vk(a){if(!a)return null;a=a.privateDoNotAccessOrElseTrustedResourceUrlWrappedValue;var b;a?b=Gb(a):b=null;return b}
;function wk(a){return Gb(null===a?"null":void 0===a?"undefined":a)}
;function xk(a){this.name=a}
;var yk=new xk("rawColdConfigGroup");var zk=new xk("rawHotConfigGroup");function Ak(a){this.F=I(a)}
w(Ak,K);var Bk=new xk("continuationCommand");var Ck=new xk("webCommandMetadata");var Dk=new xk("signalServiceEndpoint");var Ek={Df:"EMBEDDED_PLAYER_MODE_UNKNOWN",Af:"EMBEDDED_PLAYER_MODE_DEFAULT",Cf:"EMBEDDED_PLAYER_MODE_PFP",Bf:"EMBEDDED_PLAYER_MODE_PFL"};var Fk=new xk("feedbackEndpoint");function Gk(a){this.F=I(a)}
w(Gk,K);Gk.prototype.setTrackingParams=function(a){if(null!=a)if("string"===typeof a)a=a?new Ke(a,He):Ie||(Ie=new Ke(null,He));else if(a.constructor!==Ke)if(Ge(a))a=a.length?new Ke(new Uint8Array(a),He):Ie||(Ie=new Ke(null,He));else throw Error();return Of(this,1,a)};var Hk=new xk("webPlayerShareEntityServiceEndpoint");var Ik=new xk("playlistEditEndpoint");var Jk=new xk("modifyChannelNotificationPreferenceEndpoint");var Kk=new xk("unsubscribeEndpoint");var Lk=new xk("subscribeEndpoint");function Mk(){var a=Nk;E("yt.ads.biscotti.getId_")||D("yt.ads.biscotti.getId_",a)}
function Ok(a){D("yt.ads.biscotti.lastId_",a)}
;function Pk(a,b){1<b.length?a[b[0]]=b[1]:1===b.length&&Object.assign(a,b[0])}
;var Qk=C.window,Rk,Sk,Tk=(null==Qk?void 0:null==(Rk=Qk.yt)?void 0:Rk.config_)||(null==Qk?void 0:null==(Sk=Qk.ytcfg)?void 0:Sk.data_)||{};D("yt.config_",Tk);function Uk(){Pk(Tk,arguments)}
function R(a,b){return a in Tk?Tk[a]:b}
function Vk(a){var b=Tk.EXPERIMENT_FLAGS;return b?b[a]:void 0}
;var Wk=[];function Xk(a){Wk.forEach(function(b){return b(a)})}
function Yk(a){return a&&window.yterr?function(){try{return a.apply(this,arguments)}catch(b){Zk(b)}}:a}
function Zk(a){var b=E("yt.logging.errors.log");b?b(a,"ERROR",void 0,void 0,void 0,void 0,void 0):(b=R("ERRORS",[]),b.push([a,"ERROR",void 0,void 0,void 0,void 0,void 0]),Uk("ERRORS",b));Xk(a)}
function $k(a,b,c,d,e){var f=E("yt.logging.errors.log");f?f(a,"WARNING",b,c,d,void 0,e):(f=R("ERRORS",[]),f.push([a,"WARNING",b,c,d,void 0,e]),Uk("ERRORS",f))}
;var al=/^[\w.]*$/,bl={q:!0,search_query:!0};function cl(a,b){b=a.split(b);for(var c={},d=0,e=b.length;d<e;d++){var f=b[d].split("=");if(1===f.length&&f[0]||2===f.length)try{var g=dl(f[0]||""),h=dl(f[1]||"");if(g in c){var k=c[g];Array.isArray(k)?mb(k,h):c[g]=[k,h]}else c[g]=h}catch(r){var l=r,n=f[0],p=String(cl);l.args=[{key:n,value:f[1],query:a,method:el===p?"unchanged":p}];bl.hasOwnProperty(n)||$k(l)}}return c}
var el=String(cl);function fl(a){var b=[];nb(a,function(c,d){var e=encodeURIComponent(String(d));c=Array.isArray(c)?c:[c];gb(c,function(f){""==f?b.push(e):b.push(e+"="+encodeURIComponent(String(f)))})});
return b.join("&")}
function gl(a){"?"===a.charAt(0)&&(a=a.substring(1));return cl(a,"&")}
function hl(a){return-1!==a.indexOf("?")?(a=(a||"").split("#")[0],a=a.split("?",2),gl(1<a.length?a[1]:a[0])):{}}
function il(a,b,c){var d=a.split("#",2);a=d[0];d=1<d.length?"#"+d[1]:"";var e=a.split("?",2);a=e[0];e=gl(e[1]||"");for(var f in b)!c&&null!==e&&f in e||(e[f]=b[f]);return ic(a,e)+d}
function jl(a){if(!b)var b=window.location.href;var c=bc(1,a),d=cc(a);c&&d?(a=a.match($b),b=b.match($b),a=a[3]==b[3]&&a[1]==b[1]&&a[4]==b[4]):a=d?cc(b)===d&&(Number(bc(4,b))||null)===(Number(bc(4,a))||null):!0;return a}
function dl(a){return a&&a.match(al)?a:decodeURIComponent(a.replace(/\+/g," "))}
;function kl(a){var b=ll;a=void 0===a?E("yt.ads.biscotti.lastId_")||"":a;var c=Object,d=c.assign,e={};e.dt=qi;e.flash="0";a:{try{var f=b.h.top.location.href}catch(Da){f=2;break a}f=f?f===b.i.location.href?0:1:2}e=(e.frm=f,e);try{e.u_tz=-(new Date).getTimezoneOffset();var g=void 0===g?Nh:g;try{var h=g.history.length}catch(Da){h=0}e.u_his=h;var k;e.u_h=null==(k=Nh.screen)?void 0:k.height;var l;e.u_w=null==(l=Nh.screen)?void 0:l.width;var n;e.u_ah=null==(n=Nh.screen)?void 0:n.availHeight;var p;e.u_aw=
null==(p=Nh.screen)?void 0:p.availWidth;var r;e.u_cd=null==(r=Nh.screen)?void 0:r.colorDepth}catch(Da){}h=b.h;try{var t=h.screenX;var x=h.screenY}catch(Da){}try{var z=h.outerWidth;var y=h.outerHeight}catch(Da){}try{var J=h.innerWidth;var G=h.innerHeight}catch(Da){}try{var M=h.screenLeft;var P=h.screenTop}catch(Da){}try{J=h.innerWidth,G=h.innerHeight}catch(Da){}try{var ea=h.screen.availWidth;var aa=h.screen.availTop}catch(Da){}t=[M,P,t,x,ea,aa,z,y,J,G];try{var U=(b.h.top||window).document,fa="CSS1Compat"==
U.compatMode?U.documentElement:U.body;var la=(new ud(fa.clientWidth,fa.clientHeight)).round()}catch(Da){la=new ud(-12245933,-12245933)}U=la;la={};var ma=void 0===ma?C:ma;fa=new wi;"SVGElement"in ma&&"createElementNS"in ma.document&&fa.set(0);x=ni();x["allow-top-navigation-by-user-activation"]&&fa.set(1);x["allow-popups-to-escape-sandbox"]&&fa.set(2);ma.crypto&&ma.crypto.subtle&&fa.set(3);"TextDecoder"in ma&&"TextEncoder"in ma&&fa.set(4);ma=xi(fa);la.bc=ma;la.bih=U.height;la.biw=U.width;la.brdim=t.join();
b=b.i;b=(la.vis=b.prerendering?3:{visible:1,hidden:2,prerender:3,preview:4,unloaded:5}[b.visibilityState||b.webkitVisibilityState||b.mozVisibilityState||""]||0,la.wgl=!!Nh.WebGLRenderingContext,la);c=d.call(c,e,b);c.ca_type="image";a&&(c.bid=a);return c}
var ll=new function(){var a=window.document;this.h=window;this.i=a};
D("yt.ads_.signals_.getAdSignalsString",function(a){return fl(kl(a))});Za();navigator.userAgent.indexOf(" (CrKey ");var ml="XMLHttpRequest"in C?function(){return new XMLHttpRequest}:null;
function nl(){if(!ml)return null;var a=ml();return"open"in a?a:null}
function ol(a){switch(a&&"status"in a?a.status:-1){case 200:case 201:case 202:case 203:case 204:case 205:case 206:case 304:return!0;default:return!1}}
;function pl(a,b){"function"===typeof a&&(a=Yk(a));return window.setTimeout(a,b)}
;var ql="client_dev_domain client_dev_expflag client_dev_regex_map client_dev_root_url client_rollout_override expflag forcedCapability jsfeat jsmode mods".split(" ");[].concat(oa(ql),["client_dev_set_cookie"]);function S(a){a=rl(a);return"string"===typeof a&&"false"===a?!1:!!a}
function T(a,b){a=rl(a);return void 0===a&&void 0!==b?b:Number(a||0)}
function rl(a){return R("EXPERIMENT_FLAGS",{})[a]}
function sl(){for(var a=[],b=R("EXPERIMENTS_FORCED_FLAGS",{}),c=v(Object.keys(b)),d=c.next();!d.done;d=c.next())d=d.value,a.push({key:d,value:String(b[d])});c=R("EXPERIMENT_FLAGS",{});d=v(Object.keys(c));for(var e=d.next();!e.done;e=d.next())e=e.value,e.startsWith("force_")&&void 0===b[e]&&a.push({key:e,value:String(c[e])});return a}
;var tl={Authorization:"AUTHORIZATION","X-Goog-EOM-Visitor-Id":"EOM_VISITOR_DATA","X-Goog-Visitor-Id":"SANDBOXED_VISITOR_ID","X-Youtube-Domain-Admin-State":"DOMAIN_ADMIN_STATE","X-Youtube-Chrome-Connected":"CHROME_CONNECTED_HEADER","X-YouTube-Client-Name":"INNERTUBE_CONTEXT_CLIENT_NAME","X-YouTube-Client-Version":"INNERTUBE_CONTEXT_CLIENT_VERSION","X-YouTube-Delegation-Context":"INNERTUBE_CONTEXT_SERIALIZED_DELEGATION_CONTEXT","X-YouTube-Device":"DEVICE","X-Youtube-Identity-Token":"ID_TOKEN","X-YouTube-Page-CL":"PAGE_CL",
"X-YouTube-Page-Label":"PAGE_BUILD_LABEL","X-YouTube-Variants-Checksum":"VARIANTS_CHECKSUM","X-Goog-AuthUser":"SESSION_INDEX","X-Goog-PageId":"DELEGATED_SESSION_ID"},ul="app debugcss debugjs expflag force_ad_params force_ad_encrypted force_viral_ad_response_params forced_experiments innertube_snapshots innertube_goldens internalcountrycode internalipoverride absolute_experiments conditional_experiments sbb sr_bns_address".split(" ").concat(oa(ql)),vl=!1;
function wl(a,b,c,d,e,f,g,h){function k(){4===(l&&"readyState"in l?l.readyState:0)&&b&&Yk(b)(l)}
c=void 0===c?"GET":c;d=void 0===d?"":d;h=void 0===h?!1:h;var l=nl();if(!l)return null;"onloadend"in l?l.addEventListener("loadend",k,!1):l.onreadystatechange=k;S("debug_forward_web_query_parameters")&&(a=xl(a));l.open(c,a,!0);f&&(l.responseType=f);g&&(l.withCredentials=!0);c="POST"===c&&(void 0===window.FormData||!(d instanceof FormData));if(e=yl(a,e))for(var n in e)l.setRequestHeader(n,e[n]),"content-type"===n.toLowerCase()&&(c=!1);c&&l.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
if(h&&"setAttributionReporting"in XMLHttpRequest.prototype){a={eventSourceEligible:!0,triggerEligible:!1};try{l.setAttributionReporting(a)}catch(p){$k(p)}}l.send(d);return l}
function yl(a,b){b=void 0===b?{}:b;var c=jl(a),d=S("web_ajax_ignore_global_headers_if_set"),e;for(e in tl){var f=R(tl[e]),g="X-Goog-AuthUser"===e||"X-Goog-PageId"===e;"X-Goog-Visitor-Id"!==e||f||(f=R("VISITOR_DATA"));!f||!c&&cc(a)||d&&void 0!==b[e]||"TVHTML5_UNPLUGGED"===R("INNERTUBE_CLIENT_NAME")&&g||(b[e]=f)}"X-Goog-EOM-Visitor-Id"in b&&"X-Goog-Visitor-Id"in b&&delete b["X-Goog-Visitor-Id"];if(c||!cc(a))b["X-YouTube-Utc-Offset"]=String(-(new Date).getTimezoneOffset());if(c||!cc(a)){try{var h=(new Intl.DateTimeFormat).resolvedOptions().timeZone}catch(k){}h&&
(b["X-YouTube-Time-Zone"]=h)}document.location.hostname.endsWith("youtubeeducation.com")||!c&&cc(a)||(b["X-YouTube-Ad-Signals"]=fl(kl()));return b}
function zl(a,b){b.method="POST";b.postParams||(b.postParams={});return Al(a,b)}
function Al(a,b){var c=b.format||"JSON";a=Bl(a,b);var d=Cl(a,b),e=!1,f=Dl(a,function(k){if(!e){e=!0;h&&window.clearTimeout(h);var l=ol(k),n=null,p=400<=k.status&&500>k.status,r=500<=k.status&&600>k.status;if(l||p||r)n=El(a,c,k,b.convertToSafeHtml);l&&(l=Fl(c,k,n));n=n||{};p=b.context||C;l?b.onSuccess&&b.onSuccess.call(p,k,n):b.onError&&b.onError.call(p,k,n);b.onFinish&&b.onFinish.call(p,k,n)}},b.method,d,b.headers,b.responseType,b.withCredentials);
d=b.timeout||0;if(b.onTimeout&&0<d){var g=b.onTimeout;var h=pl(function(){e||(e=!0,f.abort(),window.clearTimeout(h),g.call(b.context||C,f))},d)}return f}
function Bl(a,b){b.includeDomain&&(a=document.location.protocol+"//"+document.location.hostname+(document.location.port?":"+document.location.port:"")+a);var c=R("XSRF_FIELD_NAME");if(b=b.urlParams)b[c]&&delete b[c],a=il(a,b||{},!0);return a}
function Cl(a,b){var c=R("XSRF_FIELD_NAME"),d=R("XSRF_TOKEN"),e=b.postBody||"",f=b.postParams,g=R("XSRF_FIELD_NAME"),h;b.headers&&(h=b.headers["Content-Type"]);b.excludeXsrf||cc(a)&&!b.withCredentials&&cc(a)!==document.location.hostname||"POST"!==b.method||h&&"application/x-www-form-urlencoded"!==h||b.postParams&&b.postParams[g]||(f||(f={}),f[c]=d);(S("ajax_parse_query_data_only_when_filled")&&f&&0<Object.keys(f).length||f)&&"string"===typeof e&&(e=gl(e),xb(e,f),e=b.postBodyFormat&&"JSON"===b.postBodyFormat?
JSON.stringify(e):hc(e));f=e||f&&!qb(f);!vl&&f&&"POST"!==b.method&&(vl=!0,Zk(Error("AJAX request with postData should use POST")));return e}
function El(a,b,c,d){var e=null;switch(b){case "JSON":try{var f=c.responseText}catch(g){throw d=Error("Error reading responseText"),d.params=a,$k(d),g;}a=c.getResponseHeader("Content-Type")||"";f&&0<=a.indexOf("json")&&(")]}'\n"===f.substring(0,5)&&(f=f.substring(5)),e=JSON.parse(f));break;case "XML":if(a=(a=c.responseXML)?Gl(a):null)e={},gb(a.getElementsByTagName("*"),function(g){e[g.tagName]=Hl(g)})}d&&Il(e);
return e}
function Il(a){if(Ra(a))for(var b in a){var c;(c="html_content"===b)||(c=b.length-5,c=0<=c&&b.indexOf("_html",c)==c);if(c){c=b;var d=a[b],e=zb();d=e?e.createHTML(d):d;a[c]=new Vb(d)}else Il(a[b])}}
function Fl(a,b,c){if(b&&204===b.status)return!0;switch(a){case "JSON":return!!c;case "XML":return 0===Number(c&&c.return_code);case "RAW":return!0;default:return!!c}}
function Gl(a){return a?(a=("responseXML"in a?a.responseXML:a).getElementsByTagName("root"))&&0<a.length?a[0]:null:null}
function Hl(a){var b="";gb(a.childNodes,function(c){b+=c.nodeValue});
return b}
function xl(a){var b=window.location.search,c=cc(a);S("debug_handle_relative_url_for_query_forward_killswitch")||!c&&jl(a)&&(c=document.location.hostname);var d=ac(bc(5,a));d=(c=c&&(c.endsWith("youtube.com")||c.endsWith("youtube-nocookie.com")))&&d&&d.startsWith("/api/");if(!c||d)return a;var e=gl(b),f={};gb(ul,function(g){e[g]&&(f[g]=e[g])});
return il(a,f||{},!1)}
var Dl=wl;var Jl=[{Ic:function(a){return"Cannot read property '"+a.key+"'"},
fc:{Error:[{regexp:/(Permission denied) to access property "([^']+)"/,groups:["reason","key"]}],TypeError:[{regexp:/Cannot read property '([^']+)' of (null|undefined)/,groups:["key","value"]},{regexp:/\u65e0\u6cd5\u83b7\u53d6\u672a\u5b9a\u4e49\u6216 (null|undefined) \u5f15\u7528\u7684\u5c5e\u6027\u201c([^\u201d]+)\u201d/,groups:["value","key"]},{regexp:/\uc815\uc758\ub418\uc9c0 \uc54a\uc74c \ub610\ub294 (null|undefined) \ucc38\uc870\uc778 '([^']+)' \uc18d\uc131\uc744 \uac00\uc838\uc62c \uc218 \uc5c6\uc2b5\ub2c8\ub2e4./,
groups:["value","key"]},{regexp:/No se puede obtener la propiedad '([^']+)' de referencia nula o sin definir/,groups:["key"]},{regexp:/Unable to get property '([^']+)' of (undefined or null) reference/,groups:["key","value"]},{regexp:/(null) is not an object \(evaluating '(?:([^.]+)\.)?([^']+)'\)/,groups:["value","base","key"]}]}},{Ic:function(a){return"Cannot call '"+a.key+"'"},
fc:{TypeError:[{regexp:/(?:([^ ]+)?\.)?([^ ]+) is not a function/,groups:["base","key"]},{regexp:/([^ ]+) called on (null or undefined)/,groups:["key","value"]},{regexp:/Object (.*) has no method '([^ ]+)'/,groups:["base","key"]},{regexp:/Object doesn't support property or method '([^ ]+)'/,groups:["key"]},{regexp:/\u30aa\u30d6\u30b8\u30a7\u30af\u30c8\u306f '([^']+)' \u30d7\u30ed\u30d1\u30c6\u30a3\u307e\u305f\u306f\u30e1\u30bd\u30c3\u30c9\u3092\u30b5\u30dd\u30fc\u30c8\u3057\u3066\u3044\u307e\u305b\u3093/,
groups:["key"]},{regexp:/\uac1c\uccb4\uac00 '([^']+)' \uc18d\uc131\uc774\ub098 \uba54\uc11c\ub4dc\ub97c \uc9c0\uc6d0\ud558\uc9c0 \uc54a\uc2b5\ub2c8\ub2e4./,groups:["key"]}]}},{Ic:function(a){return a.key+" is not defined"},
fc:{ReferenceError:[{regexp:/(.*) is not defined/,groups:["key"]},{regexp:/Can't find variable: (.*)/,groups:["key"]}]}}];var Ll={Ta:[],Qa:[{callback:Kl,weight:500}]};function Kl(a){if("JavaException"===a.name)return!0;a=a.stack;return a.includes("chrome://")||a.includes("chrome-extension://")||a.includes("moz-extension://")}
;function Ml(){this.Qa=[];this.Ta=[]}
var Nl;function Ol(){if(!Nl){var a=Nl=new Ml;a.Ta.length=0;a.Qa.length=0;Ll.Ta&&a.Ta.push.apply(a.Ta,Ll.Ta);Ll.Qa&&a.Qa.push.apply(a.Qa,Ll.Qa)}return Nl}
;var Pl=new L;function Ql(a){function b(){return a.charCodeAt(d++)}
var c=a.length,d=0;do{var e=Rl(b);if(Infinity===e)break;var f=e>>3;switch(e&7){case 0:e=Rl(b);if(2===f)return e;break;case 1:if(2===f)return;d+=8;break;case 2:e=Rl(b);if(2===f)return a.substr(d,e);d+=e;break;case 5:if(2===f)return;d+=4;break;default:return}}while(d<c)}
function Rl(a){var b=a(),c=b&127;if(128>b)return c;b=a();c|=(b&127)<<7;if(128>b)return c;b=a();c|=(b&127)<<14;if(128>b)return c;b=a();return 128>b?c|(b&127)<<21:Infinity}
;function Sl(a,b,c,d){if(a)if(Array.isArray(a)){var e=d;for(d=0;d<a.length&&!(a[d]&&(e+=Tl(d,a[d],b,c),500<e));d++);d=e}else if("object"===typeof a)for(e in a){if(a[e]){var f=e;var g=a[e],h=b,k=c;f="string"!==typeof g||"clickTrackingParams"!==f&&"trackingParams"!==f?0:(g=Ql(atob(g.replace(/-/g,"+").replace(/_/g,"/"))))?Tl(f+".ve",g,h,k):0;d+=f;d+=Tl(e,a[e],b,c);if(500<d)break}}else c[b]=Ul(a),d+=c[b].length;else c[b]=Ul(a),d+=c[b].length;return d}
function Tl(a,b,c,d){c+="."+a;a=Ul(b);d[c]=a;return c.length+a.length}
function Ul(a){try{return("string"===typeof a?a:String(JSON.stringify(a))).substr(0,500)}catch(b){return"unable to serialize "+typeof a+" ("+b.message+")"}}
;function Vl(){this.df=!0}
function Wl(){Vl.h||(Vl.h=new Vl);return Vl.h}
function Xl(a,b){a={};var c=yg([]);c&&(a.Authorization=c,c=b=null==b?void 0:b.sessionIndex,void 0===c&&(c=Number(R("SESSION_INDEX",0)),c=isNaN(c)?0:c),S("voice_search_auth_header_removal")||(a["X-Goog-AuthUser"]=c.toString()),"INNERTUBE_HOST_OVERRIDE"in Tk||(a["X-Origin"]=window.location.origin),void 0===b&&"DELEGATED_SESSION_ID"in Tk&&(a["X-Goog-PageId"]=R("DELEGATED_SESSION_ID")));return a}
;var Yl={identityType:"UNAUTHENTICATED_IDENTITY_TYPE_UNKNOWN"};function Zl(a){var b=this;this.i=void 0;this.h=!1;a.addEventListener("beforeinstallprompt",function(c){c.preventDefault();b.i=c});
a.addEventListener("appinstalled",function(){b.h=!0},{once:!0})}
function $l(){if(!C.matchMedia)return"WEB_DISPLAY_MODE_UNKNOWN";try{return C.matchMedia("(display-mode: standalone)").matches?"WEB_DISPLAY_MODE_STANDALONE":C.matchMedia("(display-mode: minimal-ui)").matches?"WEB_DISPLAY_MODE_MINIMAL_UI":C.matchMedia("(display-mode: fullscreen)").matches?"WEB_DISPLAY_MODE_FULLSCREEN":C.matchMedia("(display-mode: browser)").matches?"WEB_DISPLAY_MODE_BROWSER":"WEB_DISPLAY_MODE_UNKNOWN"}catch(a){return"WEB_DISPLAY_MODE_UNKNOWN"}}
;function am(a,b,c,d,e){ug.set(""+a,b,{Kb:c,path:"/",domain:void 0===d?"youtube.com":d,secure:void 0===e?!1:e})}
function bm(a){return ug.get(""+a,void 0)}
function cm(a,b,c){ug.remove(""+a,void 0===b?"/":b,void 0===c?"youtube.com":c)}
function dm(){if(S("embeds_web_enable_cookie_detection_fix")){if(!C.navigator.cookieEnabled)return!1}else if(!ug.isEnabled())return!1;if(ug.h.cookie)return!0;S("embeds_web_enable_cookie_detection_fix")?ug.set("TESTCOOKIESENABLED","1",{Kb:60,Oe:"none",secure:!0}):ug.set("TESTCOOKIESENABLED","1",{Kb:60});if("1"!==ug.get("TESTCOOKIESENABLED"))return!1;ug.remove("TESTCOOKIESENABLED");return!0}
;var em=E("ytglobal.prefsUserPrefsPrefs_")||{};D("ytglobal.prefsUserPrefsPrefs_",em);function fm(){this.h=R("ALT_PREF_COOKIE_NAME","PREF");this.i=R("ALT_PREF_COOKIE_DOMAIN","youtube.com");var a=bm(this.h);a&&this.parse(a)}
var gm;function hm(){gm||(gm=new fm);return gm}
m=fm.prototype;m.get=function(a,b){im(a);jm(a);a=void 0!==em[a]?em[a].toString():null;return null!=a?a:b?b:""};
m.set=function(a,b){im(a);jm(a);if(null==b)throw Error("ExpectedNotNull");em[a]=b.toString()};
function km(a){return!!((lm("f"+(Math.floor(a/31)+1))||0)&1<<a%31)}
m.remove=function(a){im(a);jm(a);delete em[a]};
m.clear=function(){for(var a in em)delete em[a]};
function jm(a){if(/^f([1-9][0-9]*)$/.test(a))throw Error("ExpectedRegexMatch: "+a);}
function im(a){if(!/^\w+$/.test(a))throw Error("ExpectedRegexMismatch: "+a);}
function lm(a){a=void 0!==em[a]?em[a].toString():null;return null!=a&&/^[A-Fa-f0-9]+$/.test(a)?parseInt(a,16):null}
m.parse=function(a){a=decodeURIComponent(a).split("&");for(var b=0;b<a.length;b++){var c=a[b].split("="),d=c[0];(c=c[1])&&(em[d]=c.toString())}};var mm={bluetooth:"CONN_DISCO",cellular:"CONN_CELLULAR_UNKNOWN",ethernet:"CONN_WIFI",none:"CONN_NONE",wifi:"CONN_WIFI",wimax:"CONN_CELLULAR_4G",other:"CONN_UNKNOWN",unknown:"CONN_UNKNOWN","slow-2g":"CONN_CELLULAR_2G","2g":"CONN_CELLULAR_2G","3g":"CONN_CELLULAR_3G","4g":"CONN_CELLULAR_4G"},nm={"slow-2g":"EFFECTIVE_CONNECTION_TYPE_SLOW_2G","2g":"EFFECTIVE_CONNECTION_TYPE_2G","3g":"EFFECTIVE_CONNECTION_TYPE_3G","4g":"EFFECTIVE_CONNECTION_TYPE_4G"};
function om(){var a=C.navigator;return a?a.connection:void 0}
function pm(){var a=om();if(a){var b=mm[a.type||"unknown"]||"CONN_UNKNOWN";a=mm[a.effectiveType||"unknown"]||"CONN_UNKNOWN";"CONN_CELLULAR_UNKNOWN"===b&&"CONN_UNKNOWN"!==a&&(b=a);if("CONN_UNKNOWN"!==b)return b;if("CONN_UNKNOWN"!==a)return a}}
function qm(){var a=om();if(null!=a&&a.effectiveType)return nm.hasOwnProperty(a.effectiveType)?nm[a.effectiveType]:"EFFECTIVE_CONNECTION_TYPE_UNKNOWN"}
;function V(a){var b=B.apply(1,arguments);var c=Error.call(this,a);this.message=c.message;"stack"in c&&(this.stack=c.stack);this.args=[].concat(oa(b))}
w(V,Error);function rm(){try{return sm(),!0}catch(a){return!1}}
function sm(a){if(void 0!==R("DATASYNC_ID"))return R("DATASYNC_ID");throw new V("Datasync ID not set",void 0===a?"unknown":a);}
;function tm(){}
function um(a,b){return vi.ab(a,0,b)}
tm.prototype.pa=function(a,b){return this.ab(a,1,b)};
tm.prototype.Bb=function(a){var b=E("yt.scheduler.instance.addImmediateJob");b?b(a):a()};var wm=T("web_emulated_idle_callback_delay",300),xm=1E3/60-3,ym=[8,5,4,3,2,1,0];
function zm(a){a=void 0===a?{}:a;H.call(this);this.i=[];this.j={};this.ba=this.h=0;this.Y=this.m=!1;this.S=[];this.V=this.ea=!1;for(var b=v(ym),c=b.next();!c.done;c=b.next())this.i[c.value]=[];this.l=0;this.qc=a.timeout||1;this.D=xm;this.A=0;this.ta=this.De.bind(this);this.pc=this.gf.bind(this);this.Pa=this.Qd.bind(this);this.Za=this.me.bind(this);this.Qb=this.Ge.bind(this);this.Ba=!!window.requestIdleCallback&&!!window.cancelIdleCallback&&!S("disable_scheduler_requestIdleCallback");(this.ha=!1!==
a.useRaf&&!!window.requestAnimationFrame)&&document.addEventListener("visibilitychange",this.ta)}
w(zm,H);m=zm.prototype;m.Bb=function(a){var b=Za();Am(this,a);a=Za()-b;this.m||(this.D-=a)};
m.ab=function(a,b,c){++this.ba;if(10===b)return this.Bb(a),this.ba;var d=this.ba;this.j[d]=a;this.m&&!c?this.S.push({id:d,priority:b}):(this.i[b].push(d),this.Y||this.m||(0!==this.h&&Bm(this)!==this.A&&this.stop(),this.start()));return d};
m.qa=function(a){delete this.j[a]};
function Cm(a){a.S.length=0;for(var b=5;0<=b;b--)a.i[b].length=0;a.i[8].length=0;a.j={};a.stop()}
m.isHidden=function(){return!!document.hidden||!1};
function Dm(a){return!a.isHidden()&&a.ha}
function Bm(a){if(a.i[8].length){if(a.V)return 4;if(Dm(a))return 3}for(var b=5;b>=a.l;b--)if(0<a.i[b].length)return 0<b?Dm(a)?3:2:1;return 0}
m.Jb=function(a){var b=E("yt.logging.errors.log");b&&b(a)};
function Am(a,b){try{b()}catch(c){a.Jb(c)}}
function Em(a){for(var b=v(ym),c=b.next();!c.done;c=b.next())if(a.i[c.value].length)return!0;return!1}
m.me=function(a){var b=void 0;a&&(b=a.timeRemaining());this.ea=!0;Fm(this,b);this.ea=!1};
m.gf=function(){Fm(this)};
m.Qd=function(){Gm(this)};
m.Ge=function(a){this.V=!0;var b=Bm(this);4===b&&b!==this.A&&(this.stop(),this.start());Fm(this,void 0,a);this.V=!1};
m.De=function(){this.isHidden()||Gm(this);this.h&&(this.stop(),this.start())};
function Gm(a){a.stop();a.m=!0;for(var b=Za(),c=a.i[8];c.length;){var d=c.shift(),e=a.j[d];delete a.j[d];e&&Am(a,e)}Hm(a);a.m=!1;Em(a)&&a.start();b=Za()-b;a.D-=b}
function Hm(a){for(var b=0,c=a.S.length;b<c;b++){var d=a.S[b];a.i[d.priority].push(d.id)}a.S.length=0}
function Fm(a,b,c){a.V&&4===a.A&&a.h||a.stop();a.m=!0;b=Za()+(b||a.D);for(var d=a.i[5];d.length;){var e=d.shift(),f=a.j[e];delete a.j[e];if(f){e=a;try{f(c)}catch(l){e.Jb(l)}}}for(d=a.i[4];d.length;)c=d.shift(),f=a.j[c],delete a.j[c],f&&Am(a,f);d=a.ea?0:1;d=a.l>d?a.l:d;if(!(Za()>=b)){do{a:{c=a;f=d;for(e=3;e>=f;e--)for(var g=c.i[e];g.length;){var h=g.shift(),k=c.j[h];delete c.j[h];if(k){c=k;break a}}c=null}c&&Am(a,c)}while(c&&Za()<b)}a.m=!1;Hm(a);a.D=xm;Em(a)&&a.start()}
m.start=function(){this.Y=!1;if(0===this.h)switch(this.A=Bm(this),this.A){case 1:var a=this.Za;this.h=this.Ba?window.requestIdleCallback(a,{timeout:3E3}):window.setTimeout(a,wm);break;case 2:this.h=window.setTimeout(this.pc,this.qc);break;case 3:this.h=window.requestAnimationFrame(this.Qb);break;case 4:this.h=window.setTimeout(this.Pa,0)}};
m.pause=function(){this.stop();this.Y=!0};
m.stop=function(){if(this.h){switch(this.A){case 1:var a=this.h;this.Ba?window.cancelIdleCallback(a):window.clearTimeout(a);break;case 2:case 4:window.clearTimeout(this.h);break;case 3:window.cancelAnimationFrame(this.h)}this.h=0}};
m.R=function(){Cm(this);this.stop();this.ha&&document.removeEventListener("visibilitychange",this.ta);H.prototype.R.call(this)};var Im=E("yt.scheduler.instance.timerIdMap_")||{},Jm=T("kevlar_tuner_scheduler_soft_state_timer_ms",800),Km=0,Lm=0;function Mm(){var a=E("ytglobal.schedulerInstanceInstance_");if(!a||a.Z())a=new zm(R("scheduler")||{}),D("ytglobal.schedulerInstanceInstance_",a);return a}
function Nm(){Om();var a=E("ytglobal.schedulerInstanceInstance_");a&&(rc(a),D("ytglobal.schedulerInstanceInstance_",null))}
function Om(){Cm(Mm());for(var a in Im)Im.hasOwnProperty(a)&&delete Im[Number(a)]}
function Pm(a,b,c){if(!c)return c=void 0===c,-Mm().ab(a,b,c);var d=window.setTimeout(function(){var e=Mm().ab(a,b);Im[d]=e},c);
return d}
function Qm(a){Mm().Bb(a)}
function Rm(a){var b=Mm();if(0>a)b.qa(-a);else{var c=Im[a];c?(b.qa(c),delete Im[a]):window.clearTimeout(a)}}
function Sm(){Tm()}
function Tm(){window.clearTimeout(Km);Mm().start()}
function Um(){Mm().pause();window.clearTimeout(Km);Km=window.setTimeout(Sm,Jm)}
function Vm(){window.clearTimeout(Lm);Lm=window.setTimeout(function(){Wm(0)},Jm)}
function Wm(a){Vm();var b=Mm();b.l=a;b.start()}
function Xm(a){Vm();var b=Mm();b.l>a&&(b.l=a,b.start())}
function Ym(){window.clearTimeout(Lm);var a=Mm();a.l=0;a.start()}
function Zm(){E("yt.scheduler.initialized")||(D("yt.scheduler.instance.dispose",Nm),D("yt.scheduler.instance.addJob",Pm),D("yt.scheduler.instance.addImmediateJob",Qm),D("yt.scheduler.instance.cancelJob",Rm),D("yt.scheduler.instance.cancelAllJobs",Om),D("yt.scheduler.instance.start",Tm),D("yt.scheduler.instance.pause",Um),D("yt.scheduler.instance.setPriorityThreshold",Wm),D("yt.scheduler.instance.enablePriorityThreshold",Xm),D("yt.scheduler.instance.clearPriorityThreshold",Ym),D("yt.scheduler.initialized",
!0))}
;function $m(){tm.apply(this,arguments)}
w($m,tm);function an(){$m.h||($m.h=new $m);return $m.h}
$m.prototype.ab=function(a,b,c){void 0!==c&&Number.isNaN(Number(c))&&(c=void 0);var d=E("yt.scheduler.instance.addJob");return d?d(a,b,c):void 0===c?(a(),NaN):pl(a,c||0)};
$m.prototype.qa=function(a){if(void 0===a||!Number.isNaN(Number(a))){var b=E("yt.scheduler.instance.cancelJob");b?b(a):window.clearTimeout(a)}};
$m.prototype.start=function(){var a=E("yt.scheduler.instance.start");a&&a()};
$m.prototype.pause=function(){var a=E("yt.scheduler.instance.pause");a&&a()};
var vi=an();S("web_scheduler_auto_init")&&Zm();function bn(a){var b=new Yi;(b=b.isAvailable()?a?new hj(b,a):b:null)||(a=new cj(a||"UserDataSharedStore"),b=a.isAvailable()?a:null);this.h=(a=b)?new Ti(a):null;this.i=document.domain||window.location.hostname}
bn.prototype.set=function(a,b,c,d){c=c||31104E3;this.remove(a);if(this.h)try{this.h.set(a,b,Date.now()+1E3*c);return}catch(f){}var e="";if(d)try{e=escape((new gh).serialize(b))}catch(f){return}else e=escape(b);am(a,e,c,this.i)};
bn.prototype.get=function(a,b){var c=void 0,d=!this.h;if(!d)try{c=this.h.get(a)}catch(e){d=!0}if(d&&(c=bm(a))&&(c=unescape(c),b))try{c=JSON.parse(c)}catch(e){this.remove(a),c=void 0}return c};
bn.prototype.remove=function(a){this.h&&this.h.remove(a);cm(a,"/",this.i)};var cn=function(){var a;return function(){a||(a=new bn("ytidb"));return a}}();
function dn(){var a;return null==(a=cn())?void 0:a.get("LAST_RESULT_ENTRY_KEY",!0)}
;var en=[],fn,gn=!1;function hn(){var a={};for(fn=new jn(void 0===a.handleError?kn:a.handleError,void 0===a.logEvent?ln:a.logEvent);0<en.length;)switch(a=en.shift(),a.type){case "ERROR":fn.Jb(a.payload);break;case "EVENT":fn.logEvent(a.eventType,a.payload)}}
function mn(a){gn||(fn?fn.Jb(a):(en.push({type:"ERROR",payload:a}),10<en.length&&en.shift()))}
function nn(a,b){gn||(fn?fn.logEvent(a,b):(en.push({type:"EVENT",eventType:a,payload:b}),10<en.length&&en.shift()))}
;function on(a){if(0<=a.indexOf(":"))throw Error("Database name cannot contain ':'");}
function pn(a){return a.substr(0,a.indexOf(":"))||a}
;var qn=re||se;function rn(a){var b=Mb();return b?0<=b.toLowerCase().indexOf(a):!1}
;var sn={},tn=(sn.AUTH_INVALID="No user identifier specified.",sn.EXPLICIT_ABORT="Transaction was explicitly aborted.",sn.IDB_NOT_SUPPORTED="IndexedDB is not supported.",sn.MISSING_INDEX="Index not created.",sn.MISSING_OBJECT_STORES="Object stores not created.",sn.DB_DELETED_BY_MISSING_OBJECT_STORES="Database is deleted because expected object stores were not created.",sn.DB_REOPENED_BY_MISSING_OBJECT_STORES="Database is reopened because expected object stores were not created.",sn.UNKNOWN_ABORT="Transaction was aborted for unknown reasons.",
sn.QUOTA_EXCEEDED="The current transaction exceeded its quota limitations.",sn.QUOTA_MAYBE_EXCEEDED="The current transaction may have failed because of exceeding quota limitations.",sn.EXECUTE_TRANSACTION_ON_CLOSED_DB="Can't start a transaction on a closed database",sn.INCOMPATIBLE_DB_VERSION="The binary is incompatible with the database version",sn),un={},vn=(un.AUTH_INVALID="ERROR",un.EXECUTE_TRANSACTION_ON_CLOSED_DB="WARNING",un.EXPLICIT_ABORT="IGNORED",un.IDB_NOT_SUPPORTED="ERROR",un.MISSING_INDEX=
"WARNING",un.MISSING_OBJECT_STORES="ERROR",un.DB_DELETED_BY_MISSING_OBJECT_STORES="WARNING",un.DB_REOPENED_BY_MISSING_OBJECT_STORES="WARNING",un.QUOTA_EXCEEDED="WARNING",un.QUOTA_MAYBE_EXCEEDED="WARNING",un.UNKNOWN_ABORT="WARNING",un.INCOMPATIBLE_DB_VERSION="WARNING",un),wn={},xn=(wn.AUTH_INVALID=!1,wn.EXECUTE_TRANSACTION_ON_CLOSED_DB=!1,wn.EXPLICIT_ABORT=!1,wn.IDB_NOT_SUPPORTED=!1,wn.MISSING_INDEX=!1,wn.MISSING_OBJECT_STORES=!1,wn.DB_DELETED_BY_MISSING_OBJECT_STORES=!1,wn.DB_REOPENED_BY_MISSING_OBJECT_STORES=
!1,wn.QUOTA_EXCEEDED=!1,wn.QUOTA_MAYBE_EXCEEDED=!0,wn.UNKNOWN_ABORT=!0,wn.INCOMPATIBLE_DB_VERSION=!1,wn);function yn(a,b,c,d,e){b=void 0===b?{}:b;c=void 0===c?tn[a]:c;d=void 0===d?vn[a]:d;e=void 0===e?xn[a]:e;V.call(this,c,Object.assign({},{name:"YtIdbKnownError",isSw:void 0===self.document,isIframe:self!==self.top,type:a},b));this.type=a;this.message=c;this.level=d;this.h=e;Object.setPrototypeOf(this,yn.prototype)}
w(yn,V);function zn(a,b){yn.call(this,"MISSING_OBJECT_STORES",{expectedObjectStores:b,foundObjectStores:a},tn.MISSING_OBJECT_STORES);Object.setPrototypeOf(this,zn.prototype)}
w(zn,yn);function An(a,b){var c=Error.call(this);this.message=c.message;"stack"in c&&(this.stack=c.stack);this.index=a;this.objectStore=b;Object.setPrototypeOf(this,An.prototype)}
w(An,Error);var Bn=["The database connection is closing","Can't start a transaction on a closed database","A mutation operation was attempted on a database that did not allow mutations"];
function Cn(a,b,c,d){b=pn(b);var e=a instanceof Error?a:Error("Unexpected error: "+a);if(e instanceof yn)return e;a={objectStoreNames:c,dbName:b,dbVersion:d};if("QuotaExceededError"===e.name)return new yn("QUOTA_EXCEEDED",a);if(te&&"UnknownError"===e.name)return new yn("QUOTA_MAYBE_EXCEEDED",a);if(e instanceof An)return new yn("MISSING_INDEX",Object.assign({},a,{objectStore:e.objectStore,index:e.index}));if("InvalidStateError"===e.name&&Bn.some(function(f){return e.message.includes(f)}))return new yn("EXECUTE_TRANSACTION_ON_CLOSED_DB",
a);
if("AbortError"===e.name)return new yn("UNKNOWN_ABORT",a,e.message);e.args=[Object.assign({},a,{name:"IdbError",sd:e.name})];e.level="WARNING";return e}
function Dn(a,b,c){var d=dn();return new yn("IDB_NOT_SUPPORTED",{context:{caller:a,publicName:b,version:c,hasSucceededOnce:null==d?void 0:d.hasSucceededOnce}})}
;function En(a){if(!a)throw Error();throw a;}
function Fn(a){return a}
function Gn(a){this.h=a}
function Hn(a){function b(e){if("PENDING"===d.state.status){d.state={status:"REJECTED",reason:e};e=v(d.i);for(var f=e.next();!f.done;f=e.next())f=f.value,f()}}
function c(e){if("PENDING"===d.state.status){d.state={status:"FULFILLED",value:e};e=v(d.h);for(var f=e.next();!f.done;f=e.next())f=f.value,f()}}
var d=this;this.state={status:"PENDING"};this.h=[];this.i=[];a=a.h;try{a(c,b)}catch(e){b(e)}}
Hn.all=function(a){return new Hn(new Gn(function(b,c){var d=[],e=a.length;0===e&&b(d);for(var f={rb:0};f.rb<a.length;f={rb:f.rb},++f.rb)Hn.resolve(a[f.rb]).then(function(g){return function(h){d[g.rb]=h;e--;0===e&&b(d)}}(f)).catch(function(g){c(g)})}))};
Hn.resolve=function(a){return new Hn(new Gn(function(b,c){a instanceof Hn?a.then(b,c):b(a)}))};
Hn.reject=function(a){return new Hn(new Gn(function(b,c){c(a)}))};
Hn.prototype.then=function(a,b){var c=this,d=null!=a?a:Fn,e=null!=b?b:En;return new Hn(new Gn(function(f,g){"PENDING"===c.state.status?(c.h.push(function(){In(c,c,d,f,g)}),c.i.push(function(){Jn(c,c,e,f,g)})):"FULFILLED"===c.state.status?In(c,c,d,f,g):"REJECTED"===c.state.status&&Jn(c,c,e,f,g)}))};
Hn.prototype.catch=function(a){return this.then(void 0,a)};
function In(a,b,c,d,e){try{if("FULFILLED"!==a.state.status)throw Error("calling handleResolve before the promise is fulfilled.");var f=c(a.state.value);f instanceof Hn?Kn(a,b,f,d,e):d(f)}catch(g){e(g)}}
function Jn(a,b,c,d,e){try{if("REJECTED"!==a.state.status)throw Error("calling handleReject before the promise is rejected.");var f=c(a.state.reason);f instanceof Hn?Kn(a,b,f,d,e):d(f)}catch(g){e(g)}}
function Kn(a,b,c,d,e){b===c?e(new TypeError("Circular promise chain detected.")):c.then(function(f){f instanceof Hn?Kn(a,b,f,d,e):d(f)},function(f){e(f)})}
;function Ln(a,b,c){function d(){c(a.error);f()}
function e(){b(a.result);f()}
function f(){try{a.removeEventListener("success",e),a.removeEventListener("error",d)}catch(g){}}
a.addEventListener("success",e);a.addEventListener("error",d)}
function Mn(a){return new Promise(function(b,c){Ln(a,b,c)})}
function Nn(a){return new Hn(new Gn(function(b,c){Ln(a,b,c)}))}
;function On(a,b){return new Hn(new Gn(function(c,d){function e(){var f=a?b(a):null;f?f.then(function(g){a=g;e()},d):c()}
e()}))}
;var Pn=window,W=Pn.ytcsi&&Pn.ytcsi.now?Pn.ytcsi.now:Pn.performance&&Pn.performance.timing&&Pn.performance.now&&Pn.performance.timing.navigationStart?function(){return Pn.performance.timing.navigationStart+Pn.performance.now()}:function(){return(new Date).getTime()};function Qn(a,b){this.h=a;this.options=b;this.transactionCount=0;this.j=Math.round(W());this.i=!1}
m=Qn.prototype;m.add=function(a,b,c){return Rn(this,[a],{mode:"readwrite",ja:!0},function(d){return d.objectStore(a).add(b,c)})};
m.clear=function(a){return Rn(this,[a],{mode:"readwrite",ja:!0},function(b){return b.objectStore(a).clear()})};
m.close=function(){this.h.close();var a;(null==(a=this.options)?0:a.closed)&&this.options.closed()};
m.count=function(a,b){return Rn(this,[a],{mode:"readonly",ja:!0},function(c){return c.objectStore(a).count(b)})};
function Sn(a,b,c){a=a.h.createObjectStore(b,c);return new Tn(a)}
m.delete=function(a,b){return Rn(this,[a],{mode:"readwrite",ja:!0},function(c){return c.objectStore(a).delete(b)})};
m.get=function(a,b){return Rn(this,[a],{mode:"readonly",ja:!0},function(c){return c.objectStore(a).get(b)})};
function Un(a,b,c){return Rn(a,[b],{mode:"readwrite",ja:!0},function(d){d=d.objectStore(b);return Nn(d.h.put(c,void 0))})}
m.objectStoreNames=function(){return Array.from(this.h.objectStoreNames)};
function Rn(a,b,c,d){var e,f,g,h,k,l,n,p,r,t,x,z;return A(function(y){switch(y.h){case 1:var J={mode:"readonly",ja:!1,tag:"IDB_TRANSACTION_TAG_UNKNOWN"};"string"===typeof c?J.mode=c:Object.assign(J,c);e=J;a.transactionCount++;f=e.ja?3:1;g=0;case 2:if(h){y.B(4);break}g++;k=Math.round(W());Ba(y,5);l=a.h.transaction(b,e.mode);J=y.yield;var G=new Vn(l);G=Wn(G,d);return J.call(y,G,7);case 7:return n=y.i,p=Math.round(W()),Xn(a,k,p,g,void 0,b.join(),e),y.return(n);case 5:r=Ca(y);t=Math.round(W());x=Cn(r,
a.h.name,b.join(),a.h.version);if((z=x instanceof yn&&!x.h)||g>=f)Xn(a,k,t,g,x,b.join(),e),h=x;y.B(2);break;case 4:return y.return(Promise.reject(h))}})}
function Xn(a,b,c,d,e,f,g){b=c-b;e?(e instanceof yn&&("QUOTA_EXCEEDED"===e.type||"QUOTA_MAYBE_EXCEEDED"===e.type)&&nn("QUOTA_EXCEEDED",{dbName:pn(a.h.name),objectStoreNames:f,transactionCount:a.transactionCount,transactionMode:g.mode}),e instanceof yn&&"UNKNOWN_ABORT"===e.type&&(c-=a.j,0>c&&c>=Math.pow(2,31)&&(c=0),nn("TRANSACTION_UNEXPECTEDLY_ABORTED",{objectStoreNames:f,transactionDuration:b,transactionCount:a.transactionCount,dbDuration:c}),a.i=!0),Yn(a,!1,d,f,b,g.tag),mn(e)):Yn(a,!0,d,f,b,g.tag)}
function Yn(a,b,c,d,e,f){nn("TRANSACTION_ENDED",{objectStoreNames:d,connectionHasUnknownAbortedTransaction:a.i,duration:e,isSuccessful:b,tryCount:c,tag:void 0===f?"IDB_TRANSACTION_TAG_UNKNOWN":f})}
m.getName=function(){return this.h.name};
function Tn(a){this.h=a}
m=Tn.prototype;m.add=function(a,b){return Nn(this.h.add(a,b))};
m.autoIncrement=function(){return this.h.autoIncrement};
m.clear=function(){return Nn(this.h.clear()).then(function(){})};
function Zn(a,b,c){a.h.createIndex(b,c,{unique:!1})}
m.count=function(a){return Nn(this.h.count(a))};
function $n(a,b){return ao(a,{query:b},function(c){return c.delete().then(function(){return bo(c)})}).then(function(){})}
m.delete=function(a){return a instanceof IDBKeyRange?$n(this,a):Nn(this.h.delete(a))};
m.get=function(a){return Nn(this.h.get(a))};
m.index=function(a){try{return new co(this.h.index(a))}catch(b){if(b instanceof Error&&"NotFoundError"===b.name)throw new An(a,this.h.name);throw b;}};
m.getName=function(){return this.h.name};
m.keyPath=function(){return this.h.keyPath};
function ao(a,b,c){a=a.h.openCursor(b.query,b.direction);return eo(a).then(function(d){return On(d,c)})}
function Vn(a){var b=this;this.h=a;this.i=new Map;this.aborted=!1;this.done=new Promise(function(c,d){b.h.addEventListener("complete",function(){c()});
b.h.addEventListener("error",function(e){e.currentTarget===e.target&&d(b.h.error)});
b.h.addEventListener("abort",function(){var e=b.h.error;if(e)d(e);else if(!b.aborted){e=yn;for(var f=b.h.objectStoreNames,g=[],h=0;h<f.length;h++){var k=f.item(h);if(null===k)throw Error("Invariant: item in DOMStringList is null");g.push(k)}e=new e("UNKNOWN_ABORT",{objectStoreNames:g.join(),dbName:b.h.db.name,mode:b.h.mode});d(e)}})})}
function Wn(a,b){var c=new Promise(function(d,e){try{b(a).then(function(f){d(f)}).catch(e)}catch(f){e(f),a.abort()}});
return Promise.all([c,a.done]).then(function(d){return v(d).next().value})}
Vn.prototype.abort=function(){this.h.abort();this.aborted=!0;throw new yn("EXPLICIT_ABORT");};
Vn.prototype.objectStore=function(a){a=this.h.objectStore(a);var b=this.i.get(a);b||(b=new Tn(a),this.i.set(a,b));return b};
function co(a){this.h=a}
m=co.prototype;m.count=function(a){return Nn(this.h.count(a))};
m.delete=function(a){return fo(this,{query:a},function(b){return b.delete().then(function(){return bo(b)})})};
m.get=function(a){return Nn(this.h.get(a))};
m.keyPath=function(){return this.h.keyPath};
m.unique=function(){return this.h.unique};
function fo(a,b,c){a=a.h.openCursor(void 0===b.query?null:b.query,void 0===b.direction?"next":b.direction);return eo(a).then(function(d){return On(d,c)})}
function go(a,b){this.request=a;this.cursor=b}
function eo(a){return Nn(a).then(function(b){return b?new go(a,b):null})}
function bo(a){a.cursor.continue(void 0);return eo(a.request)}
go.prototype.delete=function(){return Nn(this.cursor.delete()).then(function(){})};
go.prototype.getValue=function(){return this.cursor.value};
go.prototype.update=function(a){return Nn(this.cursor.update(a))};function ho(a,b,c){return new Promise(function(d,e){function f(){r||(r=new Qn(g.result,{closed:p}));return r}
var g=void 0!==b?self.indexedDB.open(a,b):self.indexedDB.open(a);var h=c.Sd,k=c.blocking,l=c.ef,n=c.upgrade,p=c.closed,r;g.addEventListener("upgradeneeded",function(t){try{if(null===t.newVersion)throw Error("Invariant: newVersion on IDbVersionChangeEvent is null");if(null===g.transaction)throw Error("Invariant: transaction on IDbOpenDbRequest is null");t.dataLoss&&"none"!==t.dataLoss&&nn("IDB_DATA_CORRUPTED",{reason:t.dataLossMessage||"unknown reason",dbName:pn(a)});var x=f(),z=new Vn(g.transaction);
n&&n(x,function(y){return t.oldVersion<y&&t.newVersion>=y},z);
z.done.catch(function(y){e(y)})}catch(y){e(y)}});
g.addEventListener("success",function(){var t=g.result;k&&t.addEventListener("versionchange",function(){k(f())});
t.addEventListener("close",function(){nn("IDB_UNEXPECTEDLY_CLOSED",{dbName:pn(a),dbVersion:t.version});l&&l()});
d(f())});
g.addEventListener("error",function(){e(g.error)});
h&&g.addEventListener("blocked",function(){h()})})}
function io(a,b,c){c=void 0===c?{}:c;return ho(a,b,c)}
function jo(a,b){b=void 0===b?{}:b;var c,d,e,f;return A(function(g){if(1==g.h)return Ba(g,2),c=self.indexedDB.deleteDatabase(a),d=b,(e=d.Sd)&&c.addEventListener("blocked",function(){e()}),g.yield(Mn(c),4);
if(2!=g.h)g.h=0,g.l=0;else throw f=Ca(g),Cn(f,a,"",-1);})}
;function ko(a,b){this.name=a;this.options=b;this.j=!0;this.v=this.l=0}
ko.prototype.i=function(a,b,c){c=void 0===c?{}:c;return io(a,b,c)};
ko.prototype.delete=function(a){a=void 0===a?{}:a;return jo(this.name,a)};
function lo(a,b){return new yn("INCOMPATIBLE_DB_VERSION",{dbName:a.name,oldVersion:a.options.version,newVersion:b})}
function mo(a,b){if(!b)throw Dn("openWithToken",pn(a.name));return a.open()}
ko.prototype.open=function(){function a(){var f,g,h,k,l,n,p,r,t,x;return A(function(z){switch(z.h){case 1:return g=null!=(f=Error().stack)?f:"",Ba(z,2),z.yield(c.i(c.name,c.options.version,e),4);case 4:for(var y=h=z.i,J=c.options,G=[],M=v(Object.keys(J.xb)),P=M.next();!P.done;P=M.next()){P=P.value;var ea=J.xb[P],aa=void 0===ea.Ie?Number.MAX_VALUE:ea.Ie;!(y.h.version>=ea.Cb)||y.h.version>=aa||y.h.objectStoreNames.contains(P)||G.push(P)}k=G;if(0===k.length){z.B(5);break}l=Object.keys(c.options.xb);
n=h.objectStoreNames();if(c.v<T("ytidb_reopen_db_retries",0))return c.v++,h.close(),mn(new yn("DB_REOPENED_BY_MISSING_OBJECT_STORES",{dbName:c.name,expectedObjectStores:l,foundObjectStores:n})),z.return(a());if(!(c.l<T("ytidb_remake_db_retries",1))){z.B(6);break}c.l++;return z.yield(c.delete(),7);case 7:return mn(new yn("DB_DELETED_BY_MISSING_OBJECT_STORES",{dbName:c.name,expectedObjectStores:l,foundObjectStores:n})),z.return(a());case 6:throw new zn(n,l);case 5:return z.return(h);case 2:p=Ca(z);
if(p instanceof DOMException?"VersionError"!==p.name:"DOMError"in self&&p instanceof DOMError?"VersionError"!==p.name:!(p instanceof Object&&"message"in p)||"An attempt was made to open a database using a lower version than the existing version."!==p.message){z.B(8);break}return z.yield(c.i(c.name,void 0,Object.assign({},e,{upgrade:void 0})),9);case 9:r=z.i;t=r.h.version;if(void 0!==c.options.version&&t>c.options.version+1)throw r.close(),c.j=!1,lo(c,t);return z.return(r);case 8:throw b(),p instanceof
Error&&!S("ytidb_async_stack_killswitch")&&(p.stack=p.stack+"\n"+g.substring(g.indexOf("\n")+1)),Cn(p,c.name,"",null!=(x=c.options.version)?x:-1);}})}
function b(){c.h===d&&(c.h=void 0)}
var c=this;if(!this.j)throw lo(this);if(this.h)return this.h;var d,e={blocking:function(f){f.close()},
closed:b,ef:b,upgrade:this.options.upgrade};return this.h=d=a()};var no=new ko("YtIdbMeta",{xb:{databases:{Cb:1}},upgrade:function(a,b){b(1)&&Sn(a,"databases",{keyPath:"actualName"})}});
function oo(a,b){var c;return A(function(d){if(1==d.h)return d.yield(mo(no,b),2);c=d.i;return d.return(Rn(c,["databases"],{ja:!0,mode:"readwrite"},function(e){var f=e.objectStore("databases");return f.get(a.actualName).then(function(g){if(g?a.actualName!==g.actualName||a.publicName!==g.publicName||a.userIdentifier!==g.userIdentifier:1)return Nn(f.h.put(a,void 0)).then(function(){})})}))})}
function po(a,b){var c;return A(function(d){if(1==d.h)return a?d.yield(mo(no,b),2):d.return();c=d.i;return d.return(c.delete("databases",a))})}
function qo(a,b){var c,d;return A(function(e){return 1==e.h?(c=[],e.yield(mo(no,b),2)):3!=e.h?(d=e.i,e.yield(Rn(d,["databases"],{ja:!0,mode:"readonly"},function(f){c.length=0;return ao(f.objectStore("databases"),{},function(g){a(g.getValue())&&c.push(g.getValue());return bo(g)})}),3)):e.return(c)})}
function ro(a){return qo(function(b){return"LogsDatabaseV2"===b.publicName&&void 0!==b.userIdentifier},a)}
function so(a,b,c){return qo(function(d){return c?void 0!==d.userIdentifier&&!a.includes(d.userIdentifier)&&c.includes(d.publicName):void 0!==d.userIdentifier&&!a.includes(d.userIdentifier)},b)}
function to(a){var b,c;return A(function(d){if(1==d.h)return b=sm("YtIdbMeta hasAnyMeta other"),d.yield(qo(function(e){return void 0!==e.userIdentifier&&e.userIdentifier!==b},a),2);
c=d.i;return d.return(0<c.length)})}
;var uo,vo=new function(){}(new function(){});
function wo(){var a,b,c,d;return A(function(e){switch(e.h){case 1:a=dn();if(null==(b=a)?0:b.hasSucceededOnce)return e.return(!0);var f;if(f=qn)f=/WebKit\/([0-9]+)/.exec(Mb()),f=!!(f&&600<=parseInt(f[1],10));f&&(f=/WebKit\/([0-9]+)/.exec(Mb()),f=!(f&&602<=parseInt(f[1],10)));if(f||Fc)return e.return(!1);try{if(c=self,!(c.indexedDB&&c.IDBIndex&&c.IDBKeyRange&&c.IDBObjectStore))return e.return(!1)}catch(g){return e.return(!1)}if(!("IDBTransaction"in self&&"objectStoreNames"in IDBTransaction.prototype))return e.return(!1);
Ba(e,2);d={actualName:"yt-idb-test-do-not-use",publicName:"yt-idb-test-do-not-use",userIdentifier:void 0};return e.yield(oo(d,vo),4);case 4:return e.yield(po("yt-idb-test-do-not-use",vo),5);case 5:return e.return(!0);case 2:return Ca(e),e.return(!1)}})}
function xo(){if(void 0!==uo)return uo;gn=!0;return uo=wo().then(function(a){gn=!1;var b;if(null!=(b=cn())&&b.h){var c;b={hasSucceededOnce:(null==(c=dn())?void 0:c.hasSucceededOnce)||a};var d;null==(d=cn())||d.set("LAST_RESULT_ENTRY_KEY",b,2592E3,!0)}return a})}
function yo(){return E("ytglobal.idbToken_")||void 0}
function zo(){var a=yo();return a?Promise.resolve(a):xo().then(function(b){(b=b?vo:void 0)&&D("ytglobal.idbToken_",b);return b})}
;var Ao=0;function Bo(a,b){Ao||(Ao=vi.pa(function(){var c,d,e,f,g;return A(function(h){switch(h.h){case 1:return h.yield(zo(),2);case 2:c=h.i;if(!c)return h.return();d=!0;Ba(h,3);return h.yield(so(a,c,b),5);case 5:e=h.i;if(!e.length){d=!1;h.B(6);break}f=e[0];return h.yield(jo(f.actualName),7);case 7:return h.yield(po(f.actualName,c),6);case 6:h.h=4;h.l=0;break;case 3:g=Ca(h),mn(g),d=!1;case 4:vi.qa(Ao),Ao=0,d&&Bo(a,b),h.h=0}})}))}
function Co(){var a;return A(function(b){return 1==b.h?b.yield(zo(),2):(a=b.i)?b.return(to(a)):b.return(!1)})}
new Kh;function Do(a){if(!rm())throw a=new yn("AUTH_INVALID",{dbName:a}),mn(a),a;var b=sm();return{actualName:a+":"+b,publicName:a,userIdentifier:b}}
function Eo(a,b,c,d){var e,f,g,h,k,l;return A(function(n){switch(n.h){case 1:return f=null!=(e=Error().stack)?e:"",n.yield(zo(),2);case 2:g=n.i;if(!g)throw h=Dn("openDbImpl",a,b),S("ytidb_async_stack_killswitch")||(h.stack=h.stack+"\n"+f.substring(f.indexOf("\n")+1)),mn(h),h;on(a);k=c?{actualName:a,publicName:a,userIdentifier:void 0}:Do(a);Ba(n,3);return n.yield(oo(k,g),5);case 5:return n.yield(io(k.actualName,b,d),6);case 6:return n.return(n.i);case 3:return l=Ca(n),Ba(n,7),n.yield(po(k.actualName,
g),9);case 9:n.h=8;n.l=0;break;case 7:Ca(n);case 8:throw l;}})}
function Fo(a,b,c){c=void 0===c?{}:c;return Eo(a,b,!1,c)}
function Go(a,b,c){c=void 0===c?{}:c;return Eo(a,b,!0,c)}
function Ho(a,b){b=void 0===b?{}:b;var c,d;return A(function(e){if(1==e.h)return e.yield(zo(),2);if(3!=e.h){c=e.i;if(!c)return e.return();on(a);d=Do(a);return e.yield(jo(d.actualName,b),3)}return e.yield(po(d.actualName,c),0)})}
function Io(a,b,c){a=a.map(function(d){return A(function(e){return 1==e.h?e.yield(jo(d.actualName,b),2):e.yield(po(d.actualName,c),0)})});
return Promise.all(a).then(function(){})}
function Jo(){var a=void 0===a?{}:a;var b,c;return A(function(d){if(1==d.h)return d.yield(zo(),2);if(3!=d.h){b=d.i;if(!b)return d.return();on("LogsDatabaseV2");return d.yield(ro(b),3)}c=d.i;return d.yield(Io(c,a,b),0)})}
function Ko(a,b){b=void 0===b?{}:b;var c;return A(function(d){if(1==d.h)return d.yield(zo(),2);if(3!=d.h){c=d.i;if(!c)return d.return();on(a);return d.yield(jo(a,b),3)}return d.yield(po(a,c),0)})}
;function Lo(a,b){ko.call(this,a,b);this.options=b;on(a)}
w(Lo,ko);function Mo(a,b){var c;return function(){c||(c=new Lo(a,b));return c}}
Lo.prototype.i=function(a,b,c){c=void 0===c?{}:c;return(this.options.mc?Go:Fo)(a,b,Object.assign({},c))};
Lo.prototype.delete=function(a){a=void 0===a?{}:a;return(this.options.mc?Ko:Ho)(this.name,a)};
function No(a,b){return Mo(a,b)}
;var Oo={},Po=No("ytGcfConfig",{xb:(Oo.coldConfigStore={Cb:1},Oo.hotConfigStore={Cb:1},Oo),mc:!1,upgrade:function(a,b){b(1)&&(Zn(Sn(a,"hotConfigStore",{keyPath:"key",autoIncrement:!0}),"hotTimestampIndex","timestamp"),Zn(Sn(a,"coldConfigStore",{keyPath:"key",autoIncrement:!0}),"coldTimestampIndex","timestamp"))},
version:1});function Qo(a){return mo(Po(),a)}
function Ro(a,b,c){var d,e,f;return A(function(g){switch(g.h){case 1:return d={config:a,hashData:b,timestamp:W()},g.yield(Qo(c),2);case 2:return e=g.i,g.yield(e.clear("hotConfigStore"),3);case 3:return g.yield(Un(e,"hotConfigStore",d),4);case 4:return f=g.i,g.return(f)}})}
function So(a,b,c,d){var e,f,g;return A(function(h){switch(h.h){case 1:return e={config:a,hashData:b,configData:c,timestamp:W()},h.yield(Qo(d),2);case 2:return f=h.i,h.yield(f.clear("coldConfigStore"),3);case 3:return h.yield(Un(f,"coldConfigStore",e),4);case 4:return g=h.i,h.return(g)}})}
function To(a){var b,c;return A(function(d){return 1==d.h?d.yield(Qo(a),2):3!=d.h?(b=d.i,c=void 0,d.yield(Rn(b,["coldConfigStore"],{mode:"readwrite",ja:!0},function(e){return fo(e.objectStore("coldConfigStore").index("coldTimestampIndex"),{direction:"prev"},function(f){c=f.getValue()})}),3)):d.return(c)})}
function Uo(a){var b,c;return A(function(d){return 1==d.h?d.yield(Qo(a),2):3!=d.h?(b=d.i,c=void 0,d.yield(Rn(b,["hotConfigStore"],{mode:"readwrite",ja:!0},function(e){return fo(e.objectStore("hotConfigStore").index("hotTimestampIndex"),{direction:"prev"},function(f){c=f.getValue()})}),3)):d.return(c)})}
;function Vo(){H.call(this);this.i=[];this.h=[];var a=E("yt.gcf.config.hotUpdateCallbacks");a?(this.i=[].concat(oa(a)),this.h=a):(this.h=[],D("yt.gcf.config.hotUpdateCallbacks",this.h))}
w(Vo,H);Vo.prototype.R=function(){for(var a=v(this.i),b=a.next();!b.done;b=a.next()){var c=this.h;b=c.indexOf(b.value);0<=b&&c.splice(b,1)}this.i.length=0;H.prototype.R.call(this)};function Wo(){this.h=0;this.i=new Vo}
function Xo(){var a;return null!=(a=E("yt.gcf.config.hotConfigGroup"))?a:R("RAW_HOT_CONFIG_GROUP")}
function Yo(a,b,c){var d,e,f;return A(function(g){switch(g.h){case 1:if(!S("start_client_gcf")){g.B(0);break}c&&(a.j=c,D("yt.gcf.config.hotConfigGroup",a.j||null));a.l(b);d=yo();if(!d){g.B(3);break}if(c){g.B(4);break}return g.yield(Uo(d),5);case 5:e=g.i,c=null==(f=e)?void 0:f.config;case 4:return g.yield(Ro(c,b,d),3);case 3:if(c)for(var h=c,k=v(a.i.h),l=k.next();!l.done;l=k.next())l=l.value,l(h);g.h=0}})}
function Zo(a,b,c){var d,e,f,g;return A(function(h){if(1==h.h){if(!S("start_client_gcf"))return h.B(0);a.coldHashData=b;D("yt.gcf.config.coldHashData",a.coldHashData||null);return(d=yo())?c?h.B(4):h.yield(To(d),5):h.B(0)}4!=h.h&&(e=h.i,c=null==(f=e)?void 0:f.config);if(!c)return h.B(0);g=c.configData;return h.yield(So(c,b,g,d),0)})}
function $o(){if(!Wo.h){var a=new Wo;Wo.h=a}a=Wo.h;var b=W()-a.h;if(!(0!==a.h&&b<T("send_config_hash_timer"))){b=E("yt.gcf.config.coldConfigData");var c=E("yt.gcf.config.hotHashData"),d=E("yt.gcf.config.coldHashData");b&&c&&d&&(a.h=W());return{coldConfigData:b,hotHashData:c,coldHashData:d}}}
Wo.prototype.l=function(a){this.hotHashData=a;D("yt.gcf.config.hotHashData",this.hotHashData||null)};function ap(){return"INNERTUBE_API_KEY"in Tk&&"INNERTUBE_API_VERSION"in Tk}
function bp(){return{innertubeApiKey:R("INNERTUBE_API_KEY"),innertubeApiVersion:R("INNERTUBE_API_VERSION"),ne:R("INNERTUBE_CONTEXT_CLIENT_CONFIG_INFO"),md:R("INNERTUBE_CONTEXT_CLIENT_NAME","WEB"),Zf:R("INNERTUBE_CONTEXT_CLIENT_NAME",1),innertubeContextClientVersion:R("INNERTUBE_CONTEXT_CLIENT_VERSION"),pe:R("INNERTUBE_CONTEXT_HL"),oe:R("INNERTUBE_CONTEXT_GL"),qe:R("INNERTUBE_HOST_OVERRIDE")||"",se:!!R("INNERTUBE_USE_THIRD_PARTY_AUTH",!1),re:!!R("INNERTUBE_OMIT_API_KEY_WHEN_AUTH_HEADER_IS_PRESENT",
!1),appInstallData:R("SERIALIZED_CLIENT_CONFIG_DATA")}}
function cp(a){var b={client:{hl:a.pe,gl:a.oe,clientName:a.md,clientVersion:a.innertubeContextClientVersion,configInfo:a.ne}};navigator.userAgent&&(b.client.userAgent=String(navigator.userAgent));var c=C.devicePixelRatio;c&&1!=c&&(b.client.screenDensityFloat=String(c));c=R("EXPERIMENTS_TOKEN","");""!==c&&(b.client.experimentsToken=c);c=sl();0<c.length&&(b.request={internalExperimentFlags:c});c=a.md;if(("WEB"===c||"MWEB"===c||1===c||2===c)&&b){var d;b.client.mainAppWebInfo=null!=(d=b.client.mainAppWebInfo)?
d:{};b.client.mainAppWebInfo.webDisplayMode=$l()}(d=E("yt.embedded_player.embed_url"))&&b&&(b.thirdParty={embedUrl:d});var e;if(S("web_log_memory_total_kbytes")&&(null==(e=C.navigator)?0:e.deviceMemory)){var f;e=null==(f=C.navigator)?void 0:f.deviceMemory;b&&(b.client.memoryTotalKbytes=""+1E6*e)}a.appInstallData&&b&&(b.client.configInfo=b.client.configInfo||{},b.client.configInfo.appInstallData=a.appInstallData);(a=pm())&&b&&(b.client.connectionType=a);S("web_log_effective_connection_type")&&(a=qm())&&
b&&(b.client.effectiveConnectionType=a);S("start_client_gcf")&&(e=$o())&&(a=e.coldConfigData,f=e.coldHashData,e=e.hotHashData,a&&f&&e&&b&&(b.client.configInfo=b.client.configInfo||{},b.client.configInfo.coldConfigData=a,b.client.configInfo.coldHashData=f,b.client.configInfo.hotHashData=e));R("DELEGATED_SESSION_ID")&&!S("pageid_as_header_web")&&(b.user={onBehalfOfUser:R("DELEGATED_SESSION_ID")});!S("fill_delegate_context_in_gel_killswitch")&&(a=R("INNERTUBE_CONTEXT_SERIALIZED_DELEGATION_CONTEXT"))&&
(b.user=Object.assign({},b.user,{serializedDelegationContext:a}));a=Object;f=a.assign;e=b.client;d={};c=v(Object.entries(gl(R("DEVICE",""))));for(var g=c.next();!g.done;g=c.next()){var h=v(g.value);g=h.next().value;h=h.next().value;"cbrand"===g?d.deviceMake=h:"cmodel"===g?d.deviceModel=h:"cbr"===g?d.browserName=h:"cbrver"===g?d.browserVersion=h:"cos"===g?d.osName=h:"cosver"===g?d.osVersion=h:"cplatform"===g&&(d.platform=h)}b.client=f.call(a,e,d);return b}
function dp(a,b,c){c=void 0===c?{}:c;var d={};R("EOM_VISITOR_DATA")?d={"X-Goog-EOM-Visitor-Id":R("EOM_VISITOR_DATA")}:d={"X-Goog-Visitor-Id":c.visitorData||R("VISITOR_DATA","")};if(b&&b.includes("www.youtube-nocookie.com"))return d;b=c.authorization||R("AUTHORIZATION");b||(a?b="Bearer "+E("gapi.auth.getToken")().Sf:(a=Xl(Wl()),S("pageid_as_header_web")||delete a["X-Goog-PageId"],d=Object.assign({},d,a)));b&&(d.Authorization=b);return d}
;var ep="undefined"!==typeof TextEncoder?new TextEncoder:null,fp=ep?function(a){return ep.encode(a)}:function(a){for(var b=[],c=0,d=0;d<a.length;d++){var e=a.charCodeAt(d);
128>e?b[c++]=e:(2048>e?b[c++]=e>>6|192:(55296==(e&64512)&&d+1<a.length&&56320==(a.charCodeAt(d+1)&64512)?(e=65536+((e&1023)<<10)+(a.charCodeAt(++d)&1023),b[c++]=e>>18|240,b[c++]=e>>12&63|128):b[c++]=e>>12|224,b[c++]=e>>6&63|128),b[c++]=e&63|128)}a=new Uint8Array(b.length);for(c=0;c<a.length;c++)a[c]=b[c];return a};function gp(a,b){this.version=a;this.args=b}
gp.prototype.serialize=function(){return{version:this.version,args:this.args}};function hp(a,b){this.topic=a;this.h=b}
hp.prototype.toString=function(){return this.topic};var ip=E("ytPubsub2Pubsub2Instance")||new L;L.prototype.subscribe=L.prototype.subscribe;L.prototype.unsubscribeByKey=L.prototype.Ab;L.prototype.publish=L.prototype.Ya;L.prototype.clear=L.prototype.clear;D("ytPubsub2Pubsub2Instance",ip);var jp=E("ytPubsub2Pubsub2SubscribedKeys")||{};D("ytPubsub2Pubsub2SubscribedKeys",jp);var kp=E("ytPubsub2Pubsub2TopicToKeys")||{};D("ytPubsub2Pubsub2TopicToKeys",kp);var lp=E("ytPubsub2Pubsub2IsAsync")||{};D("ytPubsub2Pubsub2IsAsync",lp);
D("ytPubsub2Pubsub2SkipSubKey",null);function mp(a,b){var c=np();c&&c.publish.call(c,a.toString(),a,b)}
function op(a){var b=pp,c=np();if(!c)return 0;var d=c.subscribe(b.toString(),function(e,f){var g=E("ytPubsub2Pubsub2SkipSubKey");g&&g==d||(g=function(){if(jp[d])try{if(f&&b instanceof hp&&b!=e)try{var h=b.h,k=f;if(!k.args||!k.version)throw Error("yt.pubsub2.Data.deserialize(): serializedData is incomplete.");try{if(!h.Wa){var l=new h;h.Wa=l.version}var n=h.Wa}catch(y){}if(!n||k.version!=n)throw Error("yt.pubsub2.Data.deserialize(): serializedData version is incompatible.");try{n=Reflect;var p=n.construct;
var r=k.args,t=r.length;if(0<t){var x=Array(t);for(k=0;k<t;k++)x[k]=r[k];var z=x}else z=[];f=p.call(n,h,z)}catch(y){throw y.message="yt.pubsub2.Data.deserialize(): "+y.message,y;}}catch(y){throw y.message="yt.pubsub2.pubsub2 cross-binary conversion error for "+b.toString()+": "+y.message,y;}a.call(window,f)}catch(y){Zk(y)}},lp[b.toString()]?E("yt.scheduler.instance")?vi.pa(g):pl(g,0):g())});
jp[d]=!0;kp[b.toString()]||(kp[b.toString()]=[]);kp[b.toString()].push(d);return d}
function qp(){var a=rp,b=op(function(c){a.apply(void 0,arguments);sp(b)});
return b}
function sp(a){var b=np();b&&("number"===typeof a&&(a=[a]),gb(a,function(c){b.unsubscribeByKey(c);delete jp[c]}))}
function np(){return E("ytPubsub2Pubsub2Instance")}
;function tp(a,b,c){c=void 0===c?{sampleRate:.1}:c;Math.random()<Math.min(.02,c.sampleRate/100)&&mp("meta_logging_csi_event",{timerName:a,pg:b})}
;var up=void 0,vp=void 0;function wp(){vp||(vp=vk(R("WORKER_SERIALIZATION_URL")));return vp||void 0}
function xp(){var a=wp();up||void 0===a||(up=new Worker(Eb(a),void 0));return up}
;var yp=T("max_body_size_to_compress",5E5),zp=T("min_body_size_to_compress",500),Ap=!0,Bp=0,Cp=0,Dp=T("compression_performance_threshold_lr",250),Ep=T("slow_compressions_before_abandon_count",4),Fp=!1,Gp=new Map,Hp=1,Ip=!0;function Jp(){if("function"===typeof Worker&&wp()&&!Fp){var a=function(c){c=c.data;if("gzippedGelBatch"===c.op){var d=Gp.get(c.key);d&&(Kp(c.gzippedBatch,d.latencyPayload,d.url,d.options,d.sendFn),Gp.delete(c.key))}},b=xp();
b&&(b.addEventListener("message",a),b.onerror=function(){Gp.clear()},Fp=!0)}}
function Lp(a,b,c,d,e){e=void 0===e?!1:e;var f={startTime:W(),ticks:{},infos:{}};if(Ap)try{var g=Mp(b);if(null!=g&&(g>yp||g<zp))d(a,c);else{if(S("gzip_gel_with_worker")&&(S("initial_gzip_use_main_thread")&&!Ip||!S("initial_gzip_use_main_thread"))){Fp||Jp();var h=xp();if(h&&!e){Gp.set(Hp,{latencyPayload:f,url:a,options:c,sendFn:d});h.postMessage({op:"gelBatchToGzip",serializedBatch:b,key:Hp});Hp++;return}}var k=uk(fp(b));Kp(k,f,a,c,d)}}catch(l){$k(l),d(a,c)}else d(a,c)}
function Kp(a,b,c,d,e){Ip=!1;var f=W();b.ticks.gelc=f;Cp++;S("disable_compression_due_to_performance_degredation")&&f-b.startTime>=Dp&&(Bp++,S("abandon_compression_after_N_slow_zips")?Cp===T("compression_disable_point")&&Bp>Ep&&(Ap=!1):Ap=!1);Np(b);d.headers||(d.headers={});d.headers["Content-Encoding"]="gzip";d.postBody=a;d.postParams=void 0;e(c,d)}
function Op(a){var b=void 0===b?!1:b;var c=void 0===c?!1:c;var d=W(),e={startTime:d,ticks:{},infos:{}},f=b?E("yt.logging.gzipForFetch",!1):!0;if(Ap&&f){if(!a.body)return a;try{var g=c?a.body:"string"===typeof a.body?a.body:JSON.stringify(a.body);f=g;if(!c&&"string"===typeof g){var h=Mp(g);if(null!=h&&(h>yp||h<zp))return a;c=b?{level:1}:void 0;f=uk(fp(g),c);var k=W();e.ticks.gelc=k;if(b){Cp++;if((S("disable_compression_due_to_performance_degredation")||S("disable_compression_due_to_performance_degradation_lr"))&&
k-d>=Dp)if(Bp++,S("abandon_compression_after_N_slow_zips")||S("abandon_compression_after_N_slow_zips_lr")){b=Bp/Cp;var l=Ep/T("compression_disable_point");0<Cp&&0===Cp%T("compression_disable_point")&&b>=l&&(Ap=!1)}else Ap=!1;Np(e)}}a.headers=Object.assign({},{"Content-Encoding":"gzip"},a.headers||{});a.body=f;return a}catch(n){return $k(n),a}}else return a}
function Mp(a){try{return(new Blob(a.split(""))).size}catch(b){return $k(b),null}}
function Np(a){S("gel_compression_csi_killswitch")||!S("log_gel_compression_latency")&&!S("log_gel_compression_latency_lr")||tp("gel_compression",a,{sampleRate:.1})}
;function Pp(a){a=Object.assign({},a);delete a.Authorization;var b=yg();if(b){var c=new Bi;c.update(R("INNERTUBE_API_KEY"));c.update(b);a.hash=we(c.digest(),3)}return a}
;var Qp;function Rp(){Qp||(Qp=new bn("yt.innertube"));return Qp}
function Sp(a,b,c,d){if(d)return null;d=Rp().get("nextId",!0)||1;var e=Rp().get("requests",!0)||{};e[d]={method:a,request:b,authState:Pp(c),requestTime:Math.round(W())};Rp().set("nextId",d+1,86400,!0);Rp().set("requests",e,86400,!0);return d}
function Tp(a){var b=Rp().get("requests",!0)||{};delete b[a];Rp().set("requests",b,86400,!0)}
function Up(a){var b=Rp().get("requests",!0);if(b){for(var c in b){var d=b[c];if(!(6E4>Math.round(W())-d.requestTime)){var e=d.authState,f=Pp(dp(!1));tb(e,f)&&(e=d.request,"requestTimeMs"in e&&(e.requestTimeMs=Math.round(W())),Vp(a,d.method,e,{}));delete b[c]}}Rp().set("requests",b,86400,!0)}}
;function Wp(a){this.Ub=this.h=!1;this.potentialEsfErrorCounter=this.i=0;this.handleError=function(){};
this.pb=function(){};
this.now=Date.now;this.Fb=!1;var b;this.Gd=null!=(b=a.Gd)?b:100;var c;this.Ad=null!=(c=a.Ad)?c:1;var d;this.yd=null!=(d=a.yd)?d:2592E6;var e;this.vd=null!=(e=a.vd)?e:12E4;var f;this.zd=null!=(f=a.zd)?f:5E3;var g;this.T=null!=(g=a.T)?g:void 0;this.Zb=!!a.Zb;var h;this.Xb=null!=(h=a.Xb)?h:.1;var k;this.ic=null!=(k=a.ic)?k:10;a.handleError&&(this.handleError=a.handleError);a.pb&&(this.pb=a.pb);a.Fb&&(this.Fb=a.Fb);a.Ub&&(this.Ub=a.Ub);this.U=a.U;this.Da=a.Da;this.da=a.da;this.aa=a.aa;this.sendFn=a.sendFn;
this.Oc=a.Oc;this.Lc=a.Lc;Xp(this)&&(!this.U||this.U("networkless_logging"))&&Yp(this)}
function Yp(a){Xp(a)&&!a.Fb&&(a.h=!0,a.Zb&&Math.random()<=a.Xb&&a.da.Td(a.T),Zp(a),a.aa.wa()&&a.Pb(),a.aa.listen(a.Oc,a.Pb.bind(a)),a.aa.listen(a.Lc,a.Zc.bind(a)))}
m=Wp.prototype;m.writeThenSend=function(a,b){var c=this;b=void 0===b?{}:b;if(Xp(this)&&this.h){var d={url:a,options:b,timestamp:this.now(),status:"NEW",sendCount:0};this.da.set(d,this.T).then(function(e){d.id=e;c.aa.wa()&&$p(c,d)}).catch(function(e){$p(c,d);
aq(c,e)})}else this.sendFn(a,b)};
m.sendThenWrite=function(a,b,c){var d=this;b=void 0===b?{}:b;if(Xp(this)&&this.h){var e={url:a,options:b,timestamp:this.now(),status:"NEW",sendCount:0};this.U&&this.U("nwl_skip_retry")&&(e.skipRetry=c);if(this.aa.wa()||this.U&&this.U("nwl_aggressive_send_then_write")&&!e.skipRetry){if(!e.skipRetry){var f=b.onError?b.onError:function(){};
b.onError=function(g,h){return A(function(k){if(1==k.h)return k.yield(d.da.set(e,d.T).catch(function(l){aq(d,l)}),2);
f(g,h);k.h=0})}}this.sendFn(a,b,e.skipRetry)}else this.da.set(e,this.T).catch(function(g){d.sendFn(a,b,e.skipRetry);
aq(d,g)})}else this.sendFn(a,b,this.U&&this.U("nwl_skip_retry")&&c)};
m.sendAndWrite=function(a,b){var c=this;b=void 0===b?{}:b;if(Xp(this)&&this.h){var d={url:a,options:b,timestamp:this.now(),status:"NEW",sendCount:0},e=!1,f=b.onSuccess?b.onSuccess:function(){};
d.options.onSuccess=function(g,h){void 0!==d.id?c.da.nb(d.id,c.T):e=!0;c.aa.gb&&c.U&&c.U("vss_network_hint")&&c.aa.gb(!0);f(g,h)};
this.sendFn(d.url,d.options,void 0,!0);this.da.set(d,this.T).then(function(g){d.id=g;e&&c.da.nb(d.id,c.T)}).catch(function(g){aq(c,g)})}else this.sendFn(a,b,void 0,!0)};
m.Pb=function(){var a=this;if(!Xp(this))throw Error("IndexedDB is not supported: throttleSend");this.i||(this.i=this.Da.pa(function(){var b;return A(function(c){if(1==c.h)return c.yield(a.da.jd("NEW",a.T),2);if(3!=c.h)return b=c.i,b?c.yield($p(a,b),3):(a.Zc(),c.return());a.i&&(a.i=0,a.Pb());c.h=0})},this.Gd))};
m.Zc=function(){this.Da.qa(this.i);this.i=0};
function $p(a,b){var c;return A(function(d){switch(d.h){case 1:if(!Xp(a))throw Error("IndexedDB is not supported: immediateSend");if(void 0===b.id){d.B(2);break}return d.yield(a.da.we(b.id,a.T),3);case 3:(c=d.i)||a.pb(Error("The request cannot be found in the database."));case 2:if(bq(a,b,a.yd)){d.B(4);break}a.pb(Error("Networkless Logging: Stored logs request expired age limit"));if(void 0===b.id){d.B(5);break}return d.yield(a.da.nb(b.id,a.T),5);case 5:return d.return();case 4:b.skipRetry||(b=cq(a,
b));if(!b){d.B(0);break}if(!b.skipRetry||void 0===b.id){d.B(8);break}return d.yield(a.da.nb(b.id,a.T),8);case 8:a.sendFn(b.url,b.options,!!b.skipRetry),d.h=0}})}
function cq(a,b){if(!Xp(a))throw Error("IndexedDB is not supported: updateRequestHandlers");var c=b.options.onError?b.options.onError:function(){};
b.options.onError=function(e,f){var g,h,k,l;return A(function(n){switch(n.h){case 1:g=dq(f);(h=eq(f))&&a.U&&a.U("web_enable_error_204")&&a.handleError(Error("Request failed due to compression"),b.url,f);if(!(a.U&&a.U("nwl_consider_error_code")&&g||a.U&&!a.U("nwl_consider_error_code")&&a.potentialEsfErrorCounter<=a.ic)){n.B(2);break}if(!a.aa.lc){n.B(3);break}return n.yield(a.aa.lc(),3);case 3:if(a.aa.wa()){n.B(2);break}c(e,f);if(!a.U||!a.U("nwl_consider_error_code")||void 0===(null==(k=b)?void 0:k.id)){n.B(6);
break}return n.yield(a.da.Pc(b.id,a.T,!1),6);case 6:return n.return();case 2:if(a.U&&a.U("nwl_consider_error_code")&&!g&&a.potentialEsfErrorCounter>a.ic)return n.return();a.potentialEsfErrorCounter++;if(void 0===(null==(l=b)?void 0:l.id)){n.B(8);break}return b.sendCount<a.Ad?n.yield(a.da.Pc(b.id,a.T,!0,h?!1:void 0),12):n.yield(a.da.nb(b.id,a.T),8);case 12:a.Da.pa(function(){a.aa.wa()&&a.Pb()},a.zd);
case 8:c(e,f),n.h=0}})};
var d=b.options.onSuccess?b.options.onSuccess:function(){};
b.options.onSuccess=function(e,f){var g;return A(function(h){if(1==h.h)return void 0===(null==(g=b)?void 0:g.id)?h.B(2):h.yield(a.da.nb(b.id,a.T),2);a.aa.gb&&a.U&&a.U("vss_network_hint")&&a.aa.gb(!0);d(e,f);h.h=0})};
return b}
function bq(a,b,c){b=b.timestamp;return a.now()-b>=c?!1:!0}
function Zp(a){if(!Xp(a))throw Error("IndexedDB is not supported: retryQueuedRequests");a.da.jd("QUEUED",a.T).then(function(b){b&&!bq(a,b,a.vd)?a.Da.pa(function(){return A(function(c){if(1==c.h)return void 0===b.id?c.B(2):c.yield(a.da.Pc(b.id,a.T),2);Zp(a);c.h=0})}):a.aa.wa()&&a.Pb()})}
function aq(a,b){a.Md&&!a.aa.wa()?a.Md(b):a.handleError(b)}
function Xp(a){return!!a.T||a.Ub}
function dq(a){var b;return(a=null==a?void 0:null==(b=a.error)?void 0:b.code)&&400<=a&&599>=a?!1:!0}
function eq(a){var b;a=null==a?void 0:null==(b=a.error)?void 0:b.code;return!(400!==a&&415!==a)}
;var fq;
function gq(){if(fq)return fq();var a={};fq=No("LogsDatabaseV2",{xb:(a.LogsRequestsStore={Cb:2},a),mc:!1,upgrade:function(b,c,d){c(2)&&Sn(b,"LogsRequestsStore",{keyPath:"id",autoIncrement:!0});c(3);c(5)&&(d=d.objectStore("LogsRequestsStore"),d.h.indexNames.contains("newRequest")&&d.h.deleteIndex("newRequest"),Zn(d,"newRequestV2",["status","interface","timestamp"]));c(7)&&b.h.objectStoreNames.contains("sapisid")&&b.h.deleteObjectStore("sapisid");c(9)&&b.h.objectStoreNames.contains("SWHealthLog")&&b.h.deleteObjectStore("SWHealthLog")},
version:9});return fq()}
;function hq(a){return mo(gq(),a)}
function iq(a,b){var c,d,e,f;return A(function(g){if(1==g.h)return c={startTime:W(),infos:{transactionType:"YT_IDB_TRANSACTION_TYPE_WRITE"},ticks:{}},g.yield(hq(b),2);if(3!=g.h)return d=g.i,e=Object.assign({},a,{options:JSON.parse(JSON.stringify(a.options)),interface:R("INNERTUBE_CONTEXT_CLIENT_NAME",0)}),g.yield(Un(d,"LogsRequestsStore",e),3);f=g.i;c.ticks.tc=W();jq(c);return g.return(f)})}
function kq(a,b){var c,d,e,f,g,h,k;return A(function(l){if(1==l.h)return c={startTime:W(),infos:{transactionType:"YT_IDB_TRANSACTION_TYPE_READ"},ticks:{}},l.yield(hq(b),2);if(3!=l.h)return d=l.i,e=R("INNERTUBE_CONTEXT_CLIENT_NAME",0),f=[a,e,0],g=[a,e,W()],h=IDBKeyRange.bound(f,g),k=void 0,l.yield(Rn(d,["LogsRequestsStore"],{mode:"readwrite",ja:!0},function(n){return fo(n.objectStore("LogsRequestsStore").index("newRequestV2"),{query:h,direction:"prev"},function(p){p.getValue()&&(k=p.getValue(),"NEW"===
a&&(k.status="QUEUED",p.update(k)))})}),3);
c.ticks.tc=W();jq(c);return l.return(k)})}
function lq(a,b){var c;return A(function(d){if(1==d.h)return d.yield(hq(b),2);c=d.i;return d.return(Rn(c,["LogsRequestsStore"],{mode:"readwrite",ja:!0},function(e){var f=e.objectStore("LogsRequestsStore");return f.get(a).then(function(g){if(g)return g.status="QUEUED",Nn(f.h.put(g,void 0)).then(function(){return g})})}))})}
function mq(a,b,c,d){c=void 0===c?!0:c;var e;return A(function(f){if(1==f.h)return f.yield(hq(b),2);e=f.i;return f.return(Rn(e,["LogsRequestsStore"],{mode:"readwrite",ja:!0},function(g){var h=g.objectStore("LogsRequestsStore");return h.get(a).then(function(k){return k?(k.status="NEW",c&&(k.sendCount+=1),void 0!==d&&(k.options.compress=d),Nn(h.h.put(k,void 0)).then(function(){return k})):Hn.resolve(void 0)})}))})}
function nq(a,b){var c;return A(function(d){if(1==d.h)return d.yield(hq(b),2);c=d.i;return d.return(c.delete("LogsRequestsStore",a))})}
function oq(a){var b,c;return A(function(d){if(1==d.h)return d.yield(hq(a),2);b=d.i;c=W()-2592E6;return d.yield(Rn(b,["LogsRequestsStore"],{mode:"readwrite",ja:!0},function(e){return ao(e.objectStore("LogsRequestsStore"),{},function(f){if(f.getValue().timestamp<=c)return f.delete().then(function(){return bo(f)})})}),0)})}
function pq(){A(function(a){return a.yield(Jo(),0)})}
function jq(a){S("nwl_csi_killswitch")||tp("networkless_performance",a,{sampleRate:1})}
;var qq={accountStateChangeSignedIn:23,accountStateChangeSignedOut:24,delayedEventMetricCaptured:11,latencyActionBaselined:6,latencyActionInfo:7,latencyActionTicked:5,offlineTransferStatusChanged:2,offlineImageDownload:335,playbackStartStateChanged:9,systemHealthCaptured:3,mangoOnboardingCompleted:10,mangoPushNotificationReceived:230,mangoUnforkDbMigrationError:121,mangoUnforkDbMigrationSummary:122,mangoUnforkDbMigrationPreunforkDbVersionNumber:133,mangoUnforkDbMigrationPhoneMetadata:134,mangoUnforkDbMigrationPhoneStorage:135,
mangoUnforkDbMigrationStep:142,mangoAsyncApiMigrationEvent:223,mangoDownloadVideoResult:224,mangoHomepageVideoCount:279,mangoHomeV3State:295,mangoImageClientCacheHitEvent:273,sdCardStatusChanged:98,framesDropped:12,thumbnailHovered:13,deviceRetentionInfoCaptured:14,thumbnailLoaded:15,backToAppEvent:318,streamingStatsCaptured:17,offlineVideoShared:19,appCrashed:20,youThere:21,offlineStateSnapshot:22,mdxSessionStarted:25,mdxSessionConnected:26,mdxSessionDisconnected:27,bedrockResourceConsumptionSnapshot:28,
nextGenWatchWatchSwiped:29,kidsAccountsSnapshot:30,zeroStepChannelCreated:31,tvhtml5SearchCompleted:32,offlineSharePairing:34,offlineShareUnlock:35,mdxRouteDistributionSnapshot:36,bedrockRepetitiveActionTimed:37,unpluggedDegradationInfo:229,uploadMp4HeaderMoved:38,uploadVideoTranscoded:39,uploadProcessorStarted:46,uploadProcessorEnded:47,uploadProcessorReady:94,uploadProcessorRequirementPending:95,uploadProcessorInterrupted:96,uploadFrontendEvent:241,assetPackDownloadStarted:41,assetPackDownloaded:42,
assetPackApplied:43,assetPackDeleted:44,appInstallAttributionEvent:459,playbackSessionStopped:45,adBlockerMessagingShown:48,distributionChannelCaptured:49,dataPlanCpidRequested:51,detailedNetworkTypeCaptured:52,sendStateUpdated:53,receiveStateUpdated:54,sendDebugStateUpdated:55,receiveDebugStateUpdated:56,kidsErrored:57,mdxMsnSessionStatsFinished:58,appSettingsCaptured:59,mdxWebSocketServerHttpError:60,mdxWebSocketServer:61,startupCrashesDetected:62,coldStartInfo:435,offlinePlaybackStarted:63,liveChatMessageSent:225,
liveChatUserPresent:434,liveChatBeingModerated:457,liveCreationCameraUpdated:64,liveCreationEncodingCaptured:65,liveCreationError:66,liveCreationHealthUpdated:67,liveCreationVideoEffectsCaptured:68,liveCreationStageOccured:75,liveCreationBroadcastScheduled:123,liveCreationArchiveReplacement:149,liveCreationCostreamingConnection:421,liveCreationStreamWebrtcStats:288,mdxSessionRecoveryStarted:69,mdxSessionRecoveryCompleted:70,mdxSessionRecoveryStopped:71,visualElementShown:72,visualElementHidden:73,
visualElementGestured:78,visualElementStateChanged:208,screenCreated:156,playbackAssociated:202,visualElementAttached:215,playbackContextEvent:214,cloudCastingPlaybackStarted:74,webPlayerApiCalled:76,tvhtml5AccountDialogOpened:79,foregroundHeartbeat:80,foregroundHeartbeatScreenAssociated:111,kidsOfflineSnapshot:81,mdxEncryptionSessionStatsFinished:82,playerRequestCompleted:83,liteSchedulerStatistics:84,mdxSignIn:85,spacecastMetadataLookupRequested:86,spacecastBatchLookupRequested:87,spacecastSummaryRequested:88,
spacecastPlayback:89,spacecastDiscovery:90,tvhtml5LaunchUrlComponentChanged:91,mdxBackgroundPlaybackRequestCompleted:92,mdxBrokenAdditionalDataDeviceDetected:93,tvhtml5LocalStorage:97,tvhtml5DeviceStorageStatus:147,autoCaptionsAvailable:99,playbackScrubbingEvent:339,flexyState:100,interfaceOrientationCaptured:101,mainAppBrowseFragmentCache:102,offlineCacheVerificationFailure:103,offlinePlaybackExceptionDigest:217,vrCopresenceStats:104,vrCopresenceSyncStats:130,vrCopresenceCommsStats:137,vrCopresencePartyStats:153,
vrCopresenceEmojiStats:213,vrCopresenceEvent:141,vrCopresenceFlowTransitEvent:160,vrCowatchPartyEvent:492,vrPlaybackEvent:345,kidsAgeGateTracking:105,offlineDelayAllowedTracking:106,mainAppAutoOfflineState:107,videoAsThumbnailDownload:108,videoAsThumbnailPlayback:109,liteShowMore:110,renderingError:118,kidsProfilePinGateTracking:119,abrTrajectory:124,scrollEvent:125,streamzIncremented:126,kidsProfileSwitcherTracking:127,kidsProfileCreationTracking:129,buyFlowStarted:136,mbsConnectionInitiated:138,
mbsPlaybackInitiated:139,mbsLoadChildren:140,liteProfileFetcher:144,mdxRemoteTransaction:146,reelPlaybackError:148,reachabilityDetectionEvent:150,mobilePlaybackEvent:151,courtsidePlayerStateChanged:152,musicPersistentCacheChecked:154,musicPersistentCacheCleared:155,playbackInterrupted:157,playbackInterruptionResolved:158,fixFopFlow:159,anrDetection:161,backstagePostCreationFlowEnded:162,clientError:163,gamingAccountLinkStatusChanged:164,liteHousewarming:165,buyFlowEvent:167,kidsParentalGateTracking:168,
kidsSignedOutSettingsStatus:437,kidsSignedOutPauseHistoryFixStatus:438,tvhtml5WatchdogViolation:444,ypcUpgradeFlow:169,yongleStudy:170,ypcUpdateFlowStarted:171,ypcUpdateFlowCancelled:172,ypcUpdateFlowSucceeded:173,ypcUpdateFlowFailed:174,liteGrowthkitPromo:175,paymentFlowStarted:341,transactionFlowShowPaymentDialog:405,transactionFlowStarted:176,transactionFlowSecondaryDeviceStarted:222,transactionFlowSecondaryDeviceSignedOutStarted:383,transactionFlowCancelled:177,transactionFlowPaymentCallBackReceived:387,
transactionFlowPaymentSubmitted:460,transactionFlowPaymentSucceeded:329,transactionFlowSucceeded:178,transactionFlowFailed:179,transactionFlowPlayBillingConnectionStartEvent:428,transactionFlowSecondaryDeviceSuccess:458,transactionFlowErrorEvent:411,liteVideoQualityChanged:180,watchBreakEnablementSettingEvent:181,watchBreakFrequencySettingEvent:182,videoEffectsCameraPerformanceMetrics:183,adNotify:184,startupTelemetry:185,playbackOfflineFallbackUsed:186,outOfMemory:187,ypcPauseFlowStarted:188,ypcPauseFlowCancelled:189,
ypcPauseFlowSucceeded:190,ypcPauseFlowFailed:191,uploadFileSelected:192,ypcResumeFlowStarted:193,ypcResumeFlowCancelled:194,ypcResumeFlowSucceeded:195,ypcResumeFlowFailed:196,adsClientStateChange:197,ypcCancelFlowStarted:198,ypcCancelFlowCancelled:199,ypcCancelFlowSucceeded:200,ypcCancelFlowFailed:201,ypcCancelFlowGoToPaymentProcessor:402,ypcDeactivateFlowStarted:320,ypcRedeemFlowStarted:203,ypcRedeemFlowCancelled:204,ypcRedeemFlowSucceeded:205,ypcRedeemFlowFailed:206,ypcFamilyCreateFlowStarted:258,
ypcFamilyCreateFlowCancelled:259,ypcFamilyCreateFlowSucceeded:260,ypcFamilyCreateFlowFailed:261,ypcFamilyManageFlowStarted:262,ypcFamilyManageFlowCancelled:263,ypcFamilyManageFlowSucceeded:264,ypcFamilyManageFlowFailed:265,restoreContextEvent:207,embedsAdEvent:327,autoplayTriggered:209,clientDataErrorEvent:210,experimentalVssValidation:211,tvhtml5TriggeredEvent:212,tvhtml5FrameworksFieldTrialResult:216,tvhtml5FrameworksFieldTrialStart:220,musicOfflinePreferences:218,watchTimeSegment:219,appWidthLayoutError:221,
accountRegistryChange:226,userMentionAutoCompleteBoxEvent:227,downloadRecommendationEnablementSettingEvent:228,musicPlaybackContentModeChangeEvent:231,offlineDbOpenCompleted:232,kidsFlowEvent:233,kidsFlowCorpusSelectedEvent:234,videoEffectsEvent:235,unpluggedOpsEogAnalyticsEvent:236,playbackAudioRouteEvent:237,interactionLoggingDebugModeError:238,offlineYtbRefreshed:239,kidsFlowError:240,musicAutoplayOnLaunchAttempted:242,deviceContextActivityEvent:243,deviceContextEvent:244,templateResolutionException:245,
musicSideloadedPlaylistServiceCalled:246,embedsStorageAccessNotChecked:247,embedsHasStorageAccessResult:248,embedsItpPlayedOnReload:249,embedsRequestStorageAccessResult:250,embedsShouldRequestStorageAccessResult:251,embedsRequestStorageAccessState:256,embedsRequestStorageAccessFailedState:257,embedsItpWatchLaterResult:266,searchSuggestDecodingPayloadFailure:252,siriShortcutActivated:253,tvhtml5KeyboardPerformance:254,latencyActionSpan:255,elementsLog:267,ytbFileOpened:268,tfliteModelError:269,apiTest:270,
yongleUsbSetup:271,touStrikeInterstitialEvent:272,liteStreamToSave:274,appBundleClientEvent:275,ytbFileCreationFailed:276,adNotifyFailure:278,ytbTransferFailed:280,blockingRequestFailed:281,liteAccountSelector:282,liteAccountUiCallbacks:283,dummyPayload:284,browseResponseValidationEvent:285,entitiesError:286,musicIosBackgroundFetch:287,mdxNotificationEvent:289,layersValidationError:290,musicPwaInstalled:291,liteAccountCleanup:292,html5PlayerHealthEvent:293,watchRestoreAttempt:294,liteAccountSignIn:296,
notaireEvent:298,kidsVoiceSearchEvent:299,adNotifyFilled:300,delayedEventDropped:301,analyticsSearchEvent:302,systemDarkThemeOptOutEvent:303,flowEvent:304,networkConnectivityBaselineEvent:305,ytbFileImported:306,downloadStreamUrlExpired:307,directSignInEvent:308,lyricImpressionEvent:309,accessibilityStateEvent:310,tokenRefreshEvent:311,genericAttestationExecution:312,tvhtml5VideoSeek:313,unpluggedAutoPause:314,scrubbingEvent:315,bedtimeReminderEvent:317,tvhtml5UnexpectedRestart:319,tvhtml5StabilityTraceEvent:478,
tvhtml5OperationHealth:467,tvhtml5WatchKeyEvent:321,voiceLanguageChanged:322,tvhtml5LiveChatStatus:323,parentToolsCorpusSelectedEvent:324,offerAdsEnrollmentInitiated:325,networkQualityIntervalEvent:326,deviceStartupMetrics:328,heartbeatActionPlayerTransitioned:330,tvhtml5Lifecycle:331,heartbeatActionPlayerHalted:332,adaptiveInlineMutedSettingEvent:333,mainAppLibraryLoadingState:334,thirdPartyLogMonitoringEvent:336,appShellAssetLoadReport:337,tvhtml5AndroidAttestation:338,tvhtml5StartupSoundEvent:340,
iosBackgroundRefreshTask:342,iosBackgroundProcessingTask:343,sliEventBatch:344,postImpressionEvent:346,musicSideloadedPlaylistExport:347,idbUnexpectedlyClosed:348,voiceSearchEvent:349,mdxSessionCastEvent:350,idbQuotaExceeded:351,idbTransactionEnded:352,idbTransactionAborted:353,tvhtml5KeyboardLogging:354,idbIsSupportedCompleted:355,creatorStudioMobileEvent:356,idbDataCorrupted:357,parentToolsAppChosenEvent:358,webViewBottomSheetResized:359,activeStateControllerScrollPerformanceSummary:360,navigatorValidation:361,
mdxSessionHeartbeat:362,clientHintsPolyfillDiagnostics:363,clientHintsPolyfillEvent:364,proofOfOriginTokenError:365,kidsAddedAccountSummary:366,musicWearableDevice:367,ypcRefundFlowEvent:368,tvhtml5PlaybackMeasurementEvent:369,tvhtml5WatermarkMeasurementEvent:370,clientExpGcfPropagationEvent:371,mainAppReferrerIntent:372,leaderLockEnded:373,leaderLockAcquired:374,googleHatsEvent:375,persistentLensLaunchEvent:376,parentToolsChildWelcomeChosenEvent:378,browseThumbnailPreloadEvent:379,finalPayload:380,
mdxDialAdditionalDataUpdateEvent:381,webOrchestrationTaskLifecycleRecord:382,startupSignalEvent:384,accountError:385,gmsDeviceCheckEvent:386,accountSelectorEvent:388,accountUiCallbacks:389,mdxDialAdditionalDataProbeEvent:390,downloadsSearchIcingApiStats:391,downloadsSearchIndexUpdatedEvent:397,downloadsSearchIndexSnapshot:398,dataPushClientEvent:392,kidsCategorySelectedEvent:393,mdxDeviceManagementSnapshotEvent:394,prefetchRequested:395,prefetchableCommandExecuted:396,gelDebuggingEvent:399,webLinkTtsPlayEnd:400,
clipViewInvalid:401,persistentStorageStateChecked:403,cacheWipeoutEvent:404,playerEvent:410,sfvEffectPipelineStartedEvent:412,sfvEffectPipelinePausedEvent:429,sfvEffectPipelineEndedEvent:413,sfvEffectChosenEvent:414,sfvEffectLoadedEvent:415,sfvEffectUserInteractionEvent:465,sfvEffectFirstFrameProcessedLatencyEvent:416,sfvEffectAggregatedFramesProcessedLatencyEvent:417,sfvEffectAggregatedFramesDroppedEvent:418,sfvEffectPipelineErrorEvent:430,sfvEffectGraphFrozenEvent:419,sfvEffectGlThreadBlockedEvent:420,
mdeVideoChangedEvent:442,mdePlayerPerformanceMetrics:472,genericClientExperimentEvent:423,homePreloadTaskScheduled:424,homePreloadTaskExecuted:425,homePreloadCacheHit:426,polymerPropertyChangedInObserver:427,applicationStarted:431,networkCronetRttBatch:432,networkCronetRttSummary:433,repeatChapterLoopEvent:436,seekCancellationEvent:462,lockModeTimeoutEvent:483,offlineTransferStarted:4,musicOfflineMixtapePreferencesChanged:16,mangoDailyNewVideosNotificationAttempt:40,mangoDailyNewVideosNotificationError:77,
dtwsPlaybackStarted:112,dtwsTileFetchStarted:113,dtwsTileFetchCompleted:114,dtwsTileFetchStatusChanged:145,dtwsKeyframeDecoderBufferSent:115,dtwsTileUnderflowedOnNonkeyframe:116,dtwsBackfillFetchStatusChanged:143,dtwsBackfillUnderflowed:117,dtwsAdaptiveLevelChanged:128,blockingVisitorIdTimeout:277,liteSocial:18,mobileJsInvocation:297,biscottiBasedDetection:439,coWatchStateChange:440,embedsVideoDataDidChange:441,shortsFirst:443,cruiseControlEvent:445,qoeClientLoggingContext:446,atvRecommendationJobExecuted:447,
tvhtml5UserFeedback:448,producerProjectCreated:449,producerProjectOpened:450,producerProjectDeleted:451,producerProjectElementAdded:453,producerProjectElementRemoved:454,tvhtml5ShowClockEvent:455,deviceCapabilityCheckMetrics:456,youtubeClearcutEvent:461,offlineBrowseFallbackEvent:463,getCtvTokenEvent:464,startupDroppedFramesSummary:466,screenshotEvent:468,miniAppPlayEvent:469,elementsDebugCounters:470,fontLoadEvent:471,webKillswitchReceived:473,webKillswitchExecuted:474,cameraOpenEvent:475,manualSmoothnessMeasurement:476,
tvhtml5AppQualityEvent:477,polymerPropertyAccessEvent:479,miniAppSdkUsage:480,cobaltTelemetryEvent:481,crossDevicePlayback:482,channelCreatedWithObakeImage:484,channelEditedWithObakeImage:485,offlineDeleteEvent:486,crossDeviceNotificationTransfer:487,androidIntentEvent:488,unpluggedAmbientInterludesCounterfactualEvent:489,keyPlaysPlayback:490,shortsCreationFallbackEvent:493,vssData:491,castMatch:494,miniAppPerformanceMetrics:495,userFeedbackEvent:496};var rq={},sq=No("ServiceWorkerLogsDatabase",{xb:(rq.SWHealthLog={Cb:1},rq),mc:!0,upgrade:function(a,b){b(1)&&Zn(Sn(a,"SWHealthLog",{keyPath:"id",autoIncrement:!0}),"swHealthNewRequest",["interface","timestamp"])},
version:1});function tq(a){return mo(sq(),a)}
function uq(a){var b,c;A(function(d){if(1==d.h)return d.yield(tq(a),2);b=d.i;c=W()-2592E6;return d.yield(Rn(b,["SWHealthLog"],{mode:"readwrite",ja:!0},function(e){return ao(e.objectStore("SWHealthLog"),{},function(f){if(f.getValue().timestamp<=c)return f.delete().then(function(){return bo(f)})})}),0)})}
function vq(a){var b;return A(function(c){if(1==c.h)return c.yield(tq(a),2);b=c.i;return c.yield(b.clear("SWHealthLog"),0)})}
;var wq={},xq=0;function yq(a){var b=new Image,c=""+xq++;wq[c]=b;b.onload=b.onerror=function(){delete wq[c]};
b.src=a}
;function zq(){this.h=new Map;this.i=!1}
function Aq(){if(!zq.h){var a=E("yt.networkRequestMonitor.instance")||new zq;D("yt.networkRequestMonitor.instance",a);zq.h=a}return zq.h}
zq.prototype.requestComplete=function(a,b){b&&(this.i=!0);a=this.removeParams(a);this.h.get(a)||this.h.set(a,b)};
zq.prototype.isEndpointCFR=function(a){a=this.removeParams(a);return(a=this.h.get(a))?!1:!1===a&&this.i?!0:null};
zq.prototype.removeParams=function(a){return a.split("?")[0]};
zq.prototype.removeParams=zq.prototype.removeParams;zq.prototype.isEndpointCFR=zq.prototype.isEndpointCFR;zq.prototype.requestComplete=zq.prototype.requestComplete;zq.getInstance=Aq;var Bq;function Cq(){Bq||(Bq=new bn("yt.offline"));return Bq}
function Dq(a){if(S("offline_error_handling")){var b=Cq().get("errors",!0)||{};b[a.message]={name:a.name,stack:a.stack};a.level&&(b[a.message].level=a.level);Cq().set("errors",b,2592E3,!0)}}
;function Eq(){od.call(this);var a=this;this.j=!1;this.i=ui();this.i.listen("networkstatus-online",function(){if(a.j&&S("offline_error_handling")){var b=Cq().get("errors",!0);if(b){for(var c in b)if(b[c]){var d=new V(c,"sent via offline_errors");d.name=b[c].name;d.stack=b[c].stack;d.level=b[c].level;Zk(d)}Cq().set("errors",{},2592E3,!0)}}})}
w(Eq,od);function Fq(){if(!Eq.h){var a=E("yt.networkStatusManager.instance")||new Eq;D("yt.networkStatusManager.instance",a);Eq.h=a}return Eq.h}
m=Eq.prototype;m.wa=function(){return this.i.wa()};
m.gb=function(a){this.i.i=a};
m.je=function(){var a=window.navigator.onLine;return void 0===a?!0:a};
m.Yd=function(){this.j=!0};
m.listen=function(a,b){return this.i.listen(a,b)};
m.lc=function(a){a=si(this.i,a);a.then(function(b){S("use_cfr_monitor")&&Aq().requestComplete("generate_204",b)});
return a};
Eq.prototype.sendNetworkCheckRequest=Eq.prototype.lc;Eq.prototype.listen=Eq.prototype.listen;Eq.prototype.enableErrorFlushing=Eq.prototype.Yd;Eq.prototype.getWindowStatus=Eq.prototype.je;Eq.prototype.networkStatusHint=Eq.prototype.gb;Eq.prototype.isNetworkAvailable=Eq.prototype.wa;Eq.getInstance=Fq;function Gq(a){a=void 0===a?{}:a;od.call(this);var b=this;this.i=this.m=0;this.j=Fq();var c=E("yt.networkStatusManager.instance.listen").bind(this.j);c&&(a.rateLimit?(this.rateLimit=a.rateLimit,c("networkstatus-online",function(){Hq(b,"publicytnetworkstatus-online")}),c("networkstatus-offline",function(){Hq(b,"publicytnetworkstatus-offline")})):(c("networkstatus-online",function(){pd(b,"publicytnetworkstatus-online")}),c("networkstatus-offline",function(){pd(b,"publicytnetworkstatus-offline")})))}
w(Gq,od);Gq.prototype.wa=function(){var a=E("yt.networkStatusManager.instance.isNetworkAvailable");return a?a.bind(this.j)():!0};
Gq.prototype.gb=function(a){var b=E("yt.networkStatusManager.instance.networkStatusHint").bind(this.j);b&&b(a)};
Gq.prototype.lc=function(a){var b=this,c;return A(function(d){c=E("yt.networkStatusManager.instance.sendNetworkCheckRequest").bind(b.j);return S("skip_network_check_if_cfr")&&Aq().isEndpointCFR("generate_204")?d.return(new Promise(function(e){var f;b.gb((null==(f=window.navigator)?void 0:f.onLine)||!0);e(b.wa())})):c?d.return(c(a)):d.return(!0)})};
function Hq(a,b){a.rateLimit?a.i?(vi.qa(a.m),a.m=vi.pa(function(){a.l!==b&&(pd(a,b),a.l=b,a.i=W())},a.rateLimit-(W()-a.i))):(pd(a,b),a.l=b,a.i=W()):pd(a,b)}
;var Iq;function Jq(){var a=Wp.call;Iq||(Iq=new Gq({eg:!0,Xf:!0}));a.call(Wp,this,{da:{Td:oq,nb:nq,jd:kq,we:lq,Pc:mq,set:iq},aa:Iq,handleError:function(b,c,d){var e,f=null==d?void 0:null==(e=d.error)?void 0:e.code;if(400===f||415===f){var g;$k(new V(b.message,c,null==d?void 0:null==(g=d.error)?void 0:g.code),void 0,void 0,void 0,!0)}else Zk(b)},
pb:$k,sendFn:Kq,now:W,Md:Dq,Da:an(),Oc:"publicytnetworkstatus-online",Lc:"publicytnetworkstatus-offline",Zb:!0,Xb:.1,ic:T("potential_esf_error_limit",10),U:S,Fb:!(rm()&&Lq())});this.j=new Kh;S("networkless_immediately_drop_all_requests")&&pq();Ko("LogsDatabaseV2")}
w(Jq,Wp);function Mq(){var a=E("yt.networklessRequestController.instance");a||(a=new Jq,D("yt.networklessRequestController.instance",a),S("networkless_logging")&&zo().then(function(b){a.T=b;Yp(a);a.j.resolve();a.Zb&&Math.random()<=a.Xb&&a.T&&uq(a.T);S("networkless_immediately_drop_sw_health_store")&&Nq(a)}));
return a}
Jq.prototype.writeThenSend=function(a,b){b||(b={});b=Oq(a,b);rm()||(this.h=!1);Wp.prototype.writeThenSend.call(this,a,b)};
Jq.prototype.sendThenWrite=function(a,b,c){b||(b={});b=Oq(a,b);rm()||(this.h=!1);Wp.prototype.sendThenWrite.call(this,a,b,c)};
Jq.prototype.sendAndWrite=function(a,b){b||(b={});b=Oq(a,b);rm()||(this.h=!1);Wp.prototype.sendAndWrite.call(this,a,b)};
Jq.prototype.awaitInitialization=function(){return this.j.promise};
function Nq(a){var b;A(function(c){if(!a.T)throw b=Dn("clearSWHealthLogsDb"),b;return c.return(vq(a.T).catch(function(d){a.handleError(d)}))})}
function Kq(a,b,c,d){d=void 0===d?!1:d;b=S("web_fp_via_jspb")?Object.assign({},b):b;S("use_cfr_monitor")&&Pq(a,b);if(S("use_request_time_ms_header"))b.headers&&jl(a)&&(b.headers["X-Goog-Request-Time"]=JSON.stringify(Math.round(W())));else{var e;if(null==(e=b.postParams)?0:e.requestTimeMs)b.postParams.requestTimeMs=Math.round(W())}if(c&&0===Object.keys(b).length){var f=void 0===f?"":f;var g=void 0===g?!1:g;var h=void 0===h?!1:h;if(a)if(f)wl(a,void 0,"POST",f,void 0);else if(R("USE_NET_AJAX_FOR_PING_TRANSPORT",
!1)||h)wl(a,void 0,"GET","",void 0,void 0,g,h);else{b:{try{var k=new cb({url:a});if(k.j&&k.i||k.l){var l=ac(bc(5,a)),n;if(!(n=!l||!l.endsWith("/aclk"))){var p=a.search(kc),r=jc(a,0,"ri",p);if(0>r)var t=null;else{var x=a.indexOf("&",r);if(0>x||x>p)x=p;t=decodeURIComponent(a.slice(r+3,-1!==x?x:0).replace(/\+/g," "))}n="1"!==t}var z=!n;break b}}catch(J){}z=!1}if(z){b:{try{if(window.navigator&&window.navigator.sendBeacon&&window.navigator.sendBeacon(a,"")){var y=!0;break b}}catch(J){}y=!1}c=y?!0:!1}else c=
!1;c||yq(a)}}else b.compress?b.postBody?("string"!==typeof b.postBody&&(b.postBody=JSON.stringify(b.postBody)),Lp(a,b.postBody,b,Al,d)):Lp(a,JSON.stringify(b.postParams),b,zl,d):Al(a,b)}
function Oq(a,b){S("use_event_time_ms_header")&&jl(a)&&(b.headers||(b.headers={}),b.headers["X-Goog-Event-Time"]=JSON.stringify(Math.round(W())));return b}
function Pq(a,b){var c=b.onError?b.onError:function(){};
b.onError=function(e,f){Aq().requestComplete(a,!1);c(e,f)};
var d=b.onSuccess?b.onSuccess:function(){};
b.onSuccess=function(e,f){Aq().requestComplete(a,!0);d(e,f)}}
function Lq(){return"www.youtube-nocookie.com"!==cc(document.location.toString())}
;var Qq=!1,Rq=C.ytNetworklessLoggingInitializationOptions||{isNwlInitialized:Qq};D("ytNetworklessLoggingInitializationOptions",Rq);function Sq(){var a;A(function(b){if(1==b.h)return b.yield(zo(),2);a=b.i;if(!a||!rm()&&!S("nwl_init_require_datasync_id_killswitch")||!Lq())return b.B(0);Qq=!0;Rq.isNwlInitialized=Qq;return b.yield(Mq().awaitInitialization(),0)})}
;function Tq(a){var b=this;this.config_=null;a?this.config_=a:ap()&&(this.config_=bp());um(function(){Up(b)},5E3)}
Tq.prototype.isReady=function(){!this.config_&&ap()&&(this.config_=bp());return!!this.config_};
function Vp(a,b,c,d){function e(x){x=void 0===x?!1:x;var z;if(d.retry&&"www.youtube-nocookie.com"!=h&&(x||S("skip_ls_gel_retry")||"application/json"!==g.headers["Content-Type"]||(z=Sp(b,c,l,k)),z)){var y=g.onSuccess,J=g.onFetchSuccess;g.onSuccess=function(P,ea){Tp(z);y(P,ea)};
c.onFetchSuccess=function(P,ea){Tp(z);J(P,ea)}}try{if(x&&d.retry&&!d.networklessOptions.bypassNetworkless)g.method="POST",d.networklessOptions.writeThenSend?Mq().writeThenSend(t,g):Mq().sendAndWrite(t,g);
else if(d.compress){var G=!d.networklessOptions.writeThenSend;if(g.postBody){var M=g.postBody;"string"!==typeof M&&(M=JSON.stringify(g.postBody));Lp(t,M,g,Al,G)}else Lp(t,JSON.stringify(g.postParams),g,zl,G)}else S("web_all_payloads_via_jspb")?Al(t,g):zl(t,g)}catch(P){if("InvalidAccessError"===P.name)z&&(Tp(z),z=0),$k(Error("An extension is blocking network request."));else throw P;}z&&um(function(){Up(a)},5E3)}
!R("VISITOR_DATA")&&"visitor_id"!==b&&.01>Math.random()&&$k(new V("Missing VISITOR_DATA when sending innertube request.",b,c,d));if(!a.isReady()){var f=new V("innertube xhrclient not ready",b,c,d);Zk(f);throw f;}var g={headers:d.headers||{},method:"POST",postParams:c,postBody:d.postBody,postBodyFormat:d.postBodyFormat||"JSON",onTimeout:function(){d.onTimeout()},
onFetchTimeout:d.onTimeout,onSuccess:function(x,z){if(d.onSuccess)d.onSuccess(z)},
onFetchSuccess:function(x){if(d.onSuccess)d.onSuccess(x)},
onError:function(x,z){if(d.onError)d.onError(z)},
onFetchError:function(x){if(d.onError)d.onError(x)},
timeout:d.timeout,withCredentials:!0,compress:d.compress};g.headers["Content-Type"]||(g.headers["Content-Type"]="application/json");var h="";(f=a.config_.qe)&&(h=f);var k=a.config_.se||!1,l=dp(k,h,d);Object.assign(g.headers,l);(f=g.headers.Authorization)&&!h&&k&&(g.headers["x-origin"]=window.location.origin);var n="/youtubei/"+a.config_.innertubeApiVersion+"/"+b,p={alt:"json"},r=a.config_.re&&f;r=r&&f.startsWith("Bearer");r||(p.key=a.config_.innertubeApiKey);var t=il(""+h+n,p||{},!0);(E("ytNetworklessLoggingInitializationOptions")?
Rq.isNwlInitialized:Qq)?xo().then(function(x){e(x)}):e(!1)}
;var Uq=0,Vq=Hc?"webkit":Gc?"moz":Ec?"ms":Dc?"o":"";D("ytDomDomGetNextId",E("ytDomDomGetNextId")||function(){return++Uq});var Wq={stopImmediatePropagation:1,stopPropagation:1,preventMouseEvent:1,preventManipulation:1,preventDefault:1,layerX:1,layerY:1,screenX:1,screenY:1,scale:1,rotation:1,webkitMovementX:1,webkitMovementY:1};
function Xq(a){this.type="";this.state=this.source=this.data=this.currentTarget=this.relatedTarget=this.target=null;this.charCode=this.keyCode=0;this.metaKey=this.shiftKey=this.ctrlKey=this.altKey=!1;this.rotation=this.clientY=this.clientX=0;this.scale=1;this.changedTouches=this.touches=null;try{if(a=a||window.event){this.event=a;for(var b in a)b in Wq||(this[b]=a[b]);this.scale=a.scale;this.rotation=a.rotation;var c=a.target||a.srcElement;c&&3==c.nodeType&&(c=c.parentNode);this.target=c;var d=a.relatedTarget;
if(d)try{d=d.nodeName?d:null}catch(e){d=null}else"mouseover"==this.type?d=a.fromElement:"mouseout"==this.type&&(d=a.toElement);this.relatedTarget=d;this.clientX=void 0!=a.clientX?a.clientX:a.pageX;this.clientY=void 0!=a.clientY?a.clientY:a.pageY;this.keyCode=a.keyCode?a.keyCode:a.which;this.charCode=a.charCode||("keypress"==this.type?this.keyCode:0);this.altKey=a.altKey;this.ctrlKey=a.ctrlKey;this.shiftKey=a.shiftKey;this.metaKey=a.metaKey;this.h=a.pageX;this.i=a.pageY}}catch(e){}}
function Yq(a){if(document.body&&document.documentElement){var b=document.body.scrollTop+document.documentElement.scrollTop;a.h=a.clientX+(document.body.scrollLeft+document.documentElement.scrollLeft);a.i=a.clientY+b}}
Xq.prototype.preventDefault=function(){this.event&&(this.event.returnValue=!1,this.event.preventDefault&&this.event.preventDefault())};
Xq.prototype.stopPropagation=function(){this.event&&(this.event.cancelBubble=!0,this.event.stopPropagation&&this.event.stopPropagation())};
Xq.prototype.stopImmediatePropagation=function(){this.event&&(this.event.cancelBubble=!0,this.event.stopImmediatePropagation&&this.event.stopImmediatePropagation())};var pb=C.ytEventsEventsListeners||{};D("ytEventsEventsListeners",pb);var Zq=C.ytEventsEventsCounter||{count:0};D("ytEventsEventsCounter",Zq);
function $q(a,b,c,d){d=void 0===d?{}:d;a.addEventListener&&("mouseenter"!=b||"onmouseenter"in document?"mouseleave"!=b||"onmouseenter"in document?"mousewheel"==b&&"MozBoxSizing"in document.documentElement.style&&(b="MozMousePixelScroll"):b="mouseout":b="mouseover");return ob(function(e){var f="boolean"===typeof e[4]&&e[4]==!!d,g=Ra(e[4])&&Ra(d)&&tb(e[4],d);return!!e.length&&e[0]==a&&e[1]==b&&e[2]==c&&(f||g)})}
var ar=eb(function(){var a=!1;try{var b=Object.defineProperty({},"capture",{get:function(){a=!0}});
window.addEventListener("test",null,b)}catch(c){}return a});
function br(a,b,c,d){d=void 0===d?{}:d;if(!a||!a.addEventListener&&!a.attachEvent)return"";var e=$q(a,b,c,d);if(e)return e;e=++Zq.count+"";var f=!("mouseenter"!=b&&"mouseleave"!=b||!a.addEventListener||"onmouseenter"in document);var g=f?function(h){h=new Xq(h);if(!xd(h.relatedTarget,function(k){return k==a}))return h.currentTarget=a,h.type=b,c.call(a,h)}:function(h){h=new Xq(h);
h.currentTarget=a;return c.call(a,h)};
g=Yk(g);a.addEventListener?("mouseenter"==b&&f?b="mouseover":"mouseleave"==b&&f?b="mouseout":"mousewheel"==b&&"MozBoxSizing"in document.documentElement.style&&(b="MozMousePixelScroll"),ar()||"boolean"===typeof d?a.addEventListener(b,g,d):a.addEventListener(b,g,!!d.capture)):a.attachEvent("on"+b,g);pb[e]=[a,b,c,g,d];return e}
function cr(a){a&&("string"==typeof a&&(a=[a]),gb(a,function(b){if(b in pb){var c=pb[b],d=c[0],e=c[1],f=c[3];c=c[4];d.removeEventListener?ar()||"boolean"===typeof c?d.removeEventListener(e,f,c):d.removeEventListener(e,f,!!c.capture):d.detachEvent&&d.detachEvent("on"+e,f);delete pb[b]}}))}
;function dr(a){this.D=a;this.h=null;this.l=0;this.A=null;this.m=0;this.i=[];for(a=0;4>a;a++)this.i.push(0);this.j=0;this.V=br(window,"mousemove",Xa(this.Y,this));a=Xa(this.S,this);"function"===typeof a&&(a=Yk(a));this.ba=window.setInterval(a,25)}
$a(dr,H);dr.prototype.Y=function(a){void 0===a.h&&Yq(a);var b=a.h;void 0===a.i&&Yq(a);this.h=new td(b,a.i)};
dr.prototype.S=function(){if(this.h){var a=W();if(0!=this.l){var b=this.A,c=this.h,d=b.x-c.x;b=b.y-c.y;d=Math.sqrt(d*d+b*b)/(a-this.l);this.i[this.j]=.5<Math.abs((d-this.m)/this.m)?1:0;for(c=b=0;4>c;c++)b+=this.i[c]||0;3<=b&&this.D();this.m=d}this.l=a;this.A=this.h;this.j=(this.j+1)%4}};
dr.prototype.R=function(){window.clearInterval(this.ba);cr(this.V)};var er={};
function fr(a){var b=void 0===a?{}:a;a=void 0===b.Fe?!1:b.Fe;b=void 0===b.Zd?!0:b.Zd;if(null==E("_lact",window)){var c=parseInt(R("LACT"),10);c=isFinite(c)?Date.now()-Math.max(c,0):-1;D("_lact",c,window);D("_fact",c,window);-1==c&&gr();br(document,"keydown",gr);br(document,"keyup",gr);br(document,"mousedown",gr);br(document,"mouseup",gr);a?br(window,"touchmove",function(){hr("touchmove",200)},{passive:!0}):(br(window,"resize",function(){hr("resize",200)}),b&&br(window,"scroll",function(){hr("scroll",200)}));
new dr(function(){hr("mouse",100)});
br(document,"touchstart",gr,{passive:!0});br(document,"touchend",gr,{passive:!0})}}
function hr(a,b){er[a]||(er[a]=!0,vi.pa(function(){gr();er[a]=!1},b))}
function gr(){null==E("_lact",window)&&fr();var a=Date.now();D("_lact",a,window);-1==E("_fact",window)&&D("_fact",a,window);(a=E("ytglobal.ytUtilActivityCallback_"))&&a()}
function ir(){var a=E("_lact",window);return null==a?-1:Math.max(Date.now()-a,0)}
;var jr=C.ytPubsubPubsubInstance||new L,kr=C.ytPubsubPubsubSubscribedKeys||{},lr=C.ytPubsubPubsubTopicToKeys||{},mr=C.ytPubsubPubsubIsSynchronous||{};function nr(a,b){var c=or();if(c&&b){var d=c.subscribe(a,function(){var e=arguments;var f=function(){kr[d]&&b.apply&&"function"==typeof b.apply&&b.apply(window,e)};
try{mr[a]?f():pl(f,0)}catch(g){Zk(g)}},void 0);
kr[d]=!0;lr[a]||(lr[a]=[]);lr[a].push(d);return d}return 0}
function pr(a){var b=or();b&&("number"===typeof a?a=[a]:"string"===typeof a&&(a=[parseInt(a,10)]),gb(a,function(c){b.unsubscribeByKey(c);delete kr[c]}))}
function tr(a,b){var c=or();c&&c.publish.apply(c,arguments)}
function ur(a){var b=or();if(b)if(b.clear(a),a)vr(a);else for(var c in lr)vr(c)}
function or(){return C.ytPubsubPubsubInstance}
function vr(a){lr[a]&&(a=lr[a],gb(a,function(b){kr[b]&&delete kr[b]}),a.length=0)}
L.prototype.subscribe=L.prototype.subscribe;L.prototype.unsubscribeByKey=L.prototype.Ab;L.prototype.publish=L.prototype.Ya;L.prototype.clear=L.prototype.clear;D("ytPubsubPubsubInstance",jr);D("ytPubsubPubsubTopicToKeys",lr);D("ytPubsubPubsubIsSynchronous",mr);D("ytPubsubPubsubSubscribedKeys",kr);var wr=Symbol("injectionDeps");function xr(a){this.name=a}
xr.prototype.toString=function(){return"InjectionToken("+this.name+")"};
function yr(a){this.key=a}
function zr(){this.i=new Map;this.j=new Map;this.h=new Map}
function Ar(a,b){a.i.set(b.kc,b);var c=a.j.get(b.kc);c&&c.lg(a.resolve(b.kc))}
zr.prototype.resolve=function(a){return a instanceof yr?Br(this,a.key,[],!0):Br(this,a,[])};
function Br(a,b,c,d){d=void 0===d?!1:d;if(-1<c.indexOf(b))throw Error("Deps cycle for: "+b);if(a.h.has(b))return a.h.get(b);if(!a.i.has(b)){if(d)return;throw Error("No provider for: "+b);}d=a.i.get(b);c.push(b);if(void 0!==d.Jd)var e=d.Jd;else if(d.lf)e=d[wr]?Cr(a,d[wr],c):[],e=d.lf.apply(d,oa(e));else if(d.Id){e=d.Id;var f=e[wr]?Cr(a,e[wr],c):[];e=new (Function.prototype.bind.apply(e,[null].concat(oa(f))))}else throw Error("Could not resolve providers for: "+b);c.pop();d.og||a.h.set(b,e);return e}
function Cr(a,b,c){return b?b.map(function(d){return d instanceof yr?Br(a,d.key,c,!0):Br(a,d,c)}):[]}
;var Dr;function Er(){Dr||(Dr=new zr);return Dr}
;var Fr=window;function Gr(){var a,b;return"h5vcc"in Fr&&(null==(a=Fr.h5vcc.traceEvent)?0:a.traceBegin)&&(null==(b=Fr.h5vcc.traceEvent)?0:b.traceEnd)?1:"performance"in Fr&&Fr.performance.mark&&Fr.performance.measure?2:0}
function Hr(a){switch(Gr()){case 1:Fr.h5vcc.traceEvent.traceBegin("YTLR",a);break;case 2:Fr.performance.mark(a+"-start");break;case 0:break;default:ci()}}
function Ir(a){switch(Gr()){case 1:Fr.h5vcc.traceEvent.traceEnd("YTLR",a);break;case 2:var b=a+"-start",c=a+"-end";Fr.performance.mark(c);Fr.performance.measure(a,b,c);break;case 0:break;default:ci()}}
;var Jr=S("web_enable_lifecycle_monitoring")&&0!==Gr(),Kr=S("web_enable_lifecycle_monitoring");function Lr(a){var b=this;var c=void 0===c?0:c;var d=void 0===d?an():d;this.j=c;this.scheduler=d;this.i=new Kh;this.h=a;for(a={cb:0};a.cb<this.h.length;a={hc:void 0,cb:a.cb},a.cb++)a.hc=this.h[a.cb],c=function(e){return function(){e.hc.Ec();b.h[e.cb].jc=!0;b.h.every(function(f){return!0===f.jc})&&b.i.resolve()}}(a),d=this.getPriority(a.hc),d=this.scheduler.ab(c,d),this.h[a.cb]=Object.assign({},a.hc,{Ec:c,
jobId:d})}
function Mr(a){var b=Array.from(a.h.keys()).sort(function(d,e){return a.getPriority(a.h[e])-a.getPriority(a.h[d])});
b=v(b);for(var c=b.next();!c.done;c=b.next())c=a.h[c.value],void 0===c.jobId||c.jc||(a.scheduler.qa(c.jobId),a.scheduler.ab(c.Ec,10))}
Lr.prototype.cancel=function(){for(var a=v(this.h),b=a.next();!b.done;b=a.next())b=b.value,void 0===b.jobId||b.jc||this.scheduler.qa(b.jobId),b.jc=!0;this.i.resolve()};
Lr.prototype.getPriority=function(a){var b;return null!=(b=a.priority)?b:this.j};function Nr(a){this.state=a;this.plugins=[];this.l=void 0;this.A={};Jr&&Hr(this.state)}
m=Nr.prototype;m.install=function(a){this.plugins.push(a);return this};
m.uninstall=function(){var a=this;B.apply(0,arguments).forEach(function(b){b=a.plugins.indexOf(b);-1<b&&a.plugins.splice(b,1)})};
m.transition=function(a,b){var c=this;Jr&&Ir(this.state);var d=this.transitions.find(function(f){return Array.isArray(f.from)?f.from.find(function(g){return g===c.state&&f.to===a}):f.from===c.state&&f.to===a});
if(d){this.j&&(Mr(this.j),this.j=void 0);Or(this,a,b);this.state=a;Jr&&Hr(this.state);d=d.action.bind(this);var e=this.plugins.filter(function(f){return f[a]}).map(function(f){return f[a]});
d(Pr(this,e),b)}else throw Error("no transition specified from "+this.state+" to "+a);};
function Pr(a,b){var c=b.filter(function(e){return 10===Qr(a,e)}),d=b.filter(function(e){return 10!==Qr(a,e)});
return a.A.ng?function(){var e=B.apply(0,arguments);return A(function(f){if(1==f.h)return f.yield(a.Me.apply(a,[c].concat(oa(e))),2);a.Dd.apply(a,[d].concat(oa(e)));f.h=0})}:function(){var e=B.apply(0,arguments);
a.Ne.apply(a,[c].concat(oa(e)));a.Dd.apply(a,[d].concat(oa(e)))}}
m.Ne=function(a){for(var b=B.apply(1,arguments),c=an(),d=v(a),e=d.next(),f={};!e.done;f={Hb:void 0},e=d.next())f.Hb=e.value,c.Bb(function(g){return function(){Rr(g.Hb.name);g.Hb.callback.apply(g.Hb,oa(b));Sr(g.Hb.name)}}(f))};
m.Me=function(a){var b=B.apply(1,arguments),c,d,e,f,g;return A(function(h){1==h.h&&(c=an(),d=v(a),e=d.next(),f={});if(3!=h.h){if(e.done)return h.B(0);f.tb=e.value;f.Sb=void 0;g=function(k){return function(){Rr(k.tb.name);var l=k.tb.callback.apply(k.tb,oa(b));"function"===typeof(null==l?void 0:l.then)?k.Sb=l.then(function(){Sr(k.tb.name)}):Sr(k.tb.name)}}(f);
c.Bb(g);return f.Sb?h.yield(f.Sb,3):h.B(3)}f={tb:void 0,Sb:void 0};e=d.next();return h.B(2)})};
m.Dd=function(a){var b=B.apply(1,arguments),c=this,d=a.map(function(e){return{Ec:function(){Rr(e.name);e.callback.apply(e,oa(b));Sr(e.name)},
priority:Qr(c,e)}});
d.length&&(this.j=new Lr(d))};
function Qr(a,b){var c,d;return null!=(d=null!=(c=a.l)?c:b.priority)?d:0}
function Rr(a){Jr&&a&&Hr(a)}
function Sr(a){Jr&&a&&Ir(a)}
function Or(a,b,c){Kr&&console.groupCollapsed&&console.groupEnd&&(console.groupCollapsed("["+a.constructor.name+"] '"+a.state+"' to '"+b+"'"),console.log("with message: ",c),console.groupEnd())}
ha.Object.defineProperties(Nr.prototype,{currentState:{configurable:!0,enumerable:!0,get:function(){return this.state}}});function Tr(a){Nr.call(this,void 0===a?"none":a);this.h=null;this.l=10;this.transitions=[{from:"none",to:"application_navigating",action:this.i},{from:"application_navigating",to:"none",action:this.v},{from:"application_navigating",to:"application_navigating",action:function(){}},
{from:"none",to:"none",action:function(){}}]}
var Ur;w(Tr,Nr);Tr.prototype.i=function(a,b){var c=this;this.h=um(function(){"application_navigating"===c.currentState&&c.transition("none")},5E3);
a(null==b?void 0:b.event)};
Tr.prototype.v=function(a,b){this.h&&(vi.qa(this.h),this.h=null);a(null==b?void 0:b.event)};
function Vr(){Ur||(Ur=new Tr);return Ur}
;var Wr=[];D("yt.logging.transport.getScrapedGelPayloads",function(){return Wr});function Xr(){this.store={};this.h={}}
Xr.prototype.storePayload=function(a,b){a=Yr(a);this.store[a]?this.store[a].push(b):(this.h={},this.store[a]=[b]);return a};
Xr.prototype.smartExtractMatchingEntries=function(a){if(!a.keys.length)return[];for(var b=Zr(this,a.keys.splice(0,1)[0]),c=[],d=0;d<b.length;d++)this.store[b[d]]&&a.sizeLimit&&(this.store[b[d]].length<=a.sizeLimit?(c.push.apply(c,oa(this.store[b[d]])),delete this.store[b[d]]):c.push.apply(c,oa(this.store[b[d]].splice(0,a.sizeLimit))));(null==a?0:a.sizeLimit)&&c.length<(null==a?void 0:a.sizeLimit)&&(a.sizeLimit-=c.length,c.push.apply(c,oa(this.smartExtractMatchingEntries(a))));return c};
Xr.prototype.extractMatchingEntries=function(a){a=Zr(this,a);for(var b=[],c=0;c<a.length;c++)this.store[a[c]]&&(b.push.apply(b,oa(this.store[a[c]])),delete this.store[a[c]]);return b};
Xr.prototype.getSequenceCount=function(a){a=Zr(this,a);for(var b=0,c=0;c<a.length;c++){var d=void 0;b+=(null==(d=this.store[a[c]])?void 0:d.length)||0}return b};
function Zr(a,b){var c=Yr(b);if(a.h[c])return a.h[c];var d=Object.keys(a.store)||[];if(1>=d.length&&Yr(b)===d[0])return d;for(var e=[],f=0;f<d.length;f++){var g=d[f].split("/");if($r(b.auth,g[0])){var h=b.isJspb;$r(void 0===h?"undefined":h?"true":"false",g[1])&&$r(b.cttAuthInfo,g[2])&&(h=b.tier,h=void 0===h?"undefined":JSON.stringify(h),$r(h,g[3])&&e.push(d[f]))}}return a.h[c]=e}
function $r(a,b){return void 0===a||"undefined"===a?!0:a===b}
Xr.prototype.getSequenceCount=Xr.prototype.getSequenceCount;Xr.prototype.extractMatchingEntries=Xr.prototype.extractMatchingEntries;Xr.prototype.smartExtractMatchingEntries=Xr.prototype.smartExtractMatchingEntries;Xr.prototype.storePayload=Xr.prototype.storePayload;function Yr(a){return[void 0===a.auth?"undefined":a.auth,void 0===a.isJspb?"undefined":a.isJspb,void 0===a.cttAuthInfo?"undefined":a.cttAuthInfo,void 0===a.tier?"undefined":a.tier].join("/")}
;function as(a,b){if(a)return a[b.name]}
;var bs=T("initial_gel_batch_timeout",2E3),cs=T("gel_queue_timeout_max_ms",6E4),ds=Math.pow(2,16)-1,es=T("gel_min_batch_size",5),gs=void 0,hs=null;function is(){this.l=this.h=this.i=0;this.j=!1}
var js=new is,ks=new is,ls=new is,ms=new is,ns,ps=!0,qs=C.ytLoggingTransportTokensToCttTargetIds_||{};D("ytLoggingTransportTokensToCttTargetIds_",qs);var rs={};function ss(){var a=E("yt.logging.ims");a||(a=new Xr,D("yt.logging.ims",a));return a}
function ts(a,b){if("log_event"===a.endpoint){us();var c=vs(a),d=ws(a.payload)||"";a:{if(S("enable_web_tiered_gel")){var e=qq[d||""];var f,g,h,k=null==Er().resolve(new yr(Wo))?void 0:null==(f=Xo())?void 0:null==(g=f.loggingHotConfig)?void 0:null==(h=g.eventLoggingConfig)?void 0:h.payloadPolicies;if(k)for(f=0;f<k.length;f++)if(k[f].payloadNumber===e){e=k[f];break a}}e=void 0}k=200;if(e){if(!1===e.enabled&&!S("web_payload_policy_disabled_killswitch"))return;k=xs(e.tier);if(400===k){ys(a,b);return}}rs[c]=
!0;e={cttAuthInfo:c,isJspb:!1,tier:k};ss().storePayload(e,a.payload);zs(b,c,e,"gelDebuggingEvent"===d)}}
function zs(a,b,c,d){function e(){As({writeThenSend:!0},S("flush_only_full_queue")?b:void 0,f,c.tier)}
var f=!1;f=void 0===f?!1:f;d=void 0===d?!1:d;S("web_enable_cached_it_client")&&a&&a!==hs?(gs=new a,hs=a):!S("web_enable_cached_it_client")&&a&&(gs=new a);a=T("tvhtml5_logging_max_batch_ads_fork")||T("web_logging_max_batch")||100;var g=W(),h=Bs(f,c.tier),k=h.l;d&&(h.j=!0);d=0;c&&(d=ss().getSequenceCount(c));1E3<=d?e():d>=a?ns||(ns=Cs(function(){e();ns=void 0},0)):10<=g-k&&(Ds(f,c.tier),h.l=g)}
function ys(a,b){if("log_event"===a.endpoint){us();var c=vs(a),d=new Map;d.set(c,[a.payload]);var e=ws(a.payload)||"";b&&(gs=new b);return new Kd(function(f,g){gs&&gs.isReady()?Es(d,gs,f,g,{bypassNetworkless:!0},!0,"gelDebuggingEvent"===e):f()})}}
function vs(a){var b="";if(a.dangerousLogToVisitorSession)b="visitorOnlyApprovedKey";else if(a.cttAuthInfo){b=a.cttAuthInfo;var c={};b.videoId?c.videoId=b.videoId:b.playlistId&&(c.playlistId=b.playlistId);qs[a.cttAuthInfo.token]=c;b=a.cttAuthInfo.token}return b}
function As(a,b,c,d){a=void 0===a?{}:a;c=void 0===c?!1:c;new Kd(function(e,f){var g=Bs(c,d),h=g.j;g.j=!1;Fs(g.i);Fs(g.h);g.h=0;gs&&gs.isReady()?void 0===d&&S("enable_web_tiered_gel")?Gs(e,f,a,b,c,300,h):Gs(e,f,a,b,c,d,h):(Ds(c,d),e())})}
function Gs(a,b,c,d,e,f,g){var h=gs;c=void 0===c?{}:c;e=void 0===e?!1:e;f=void 0===f?200:f;g=void 0===g?!1:g;var k=new Map,l={isJspb:e,cttAuthInfo:d,tier:f};e={isJspb:e,cttAuthInfo:d};if(void 0!==d)f=S("enable_web_tiered_gel")?ss().smartExtractMatchingEntries({keys:[l,e],sizeLimit:1E3}):ss().extractMatchingEntries(e),k.set(d,f);else for(d=v(Object.keys(rs)),l=d.next();!l.done;l=d.next())l=l.value,e=S("enable_web_tiered_gel")?ss().smartExtractMatchingEntries({keys:[{isJspb:!1,cttAuthInfo:l,tier:f},
{isJspb:!1,cttAuthInfo:l}],sizeLimit:1E3}):ss().extractMatchingEntries({isJspb:!1,cttAuthInfo:l}),0<e.length&&k.set(l,e),(S("web_fp_via_jspb_and_json")&&c.writeThenSend||!S("web_fp_via_jspb_and_json"))&&delete rs[l];Es(k,h,a,b,c,!1,g)}
function Ds(a,b){function c(){As({writeThenSend:!0},void 0,a,b)}
a=void 0===a?!1:a;b=void 0===b?200:b;var d=Bs(a,b),e=d===ms||d===ls?5E3:cs;S("web_gel_timeout_cap")&&!d.h&&(e=Cs(function(){c()},e),d.h=e);
Fs(d.i);e=R("LOGGING_BATCH_TIMEOUT",T("web_gel_debounce_ms",1E4));S("shorten_initial_gel_batch_timeout")&&ps&&(e=bs);e=Cs(function(){0<T("gel_min_batch_size")?ss().getSequenceCount({cttAuthInfo:void 0,isJspb:a,tier:b})>=es&&c():c()},e);
d.i=e}
function Es(a,b,c,d,e,f,g){e=void 0===e?{}:e;var h=Math.round(W()),k=a.size,l=(void 0===g?0:g)&&S("vss_through_gel_video_stats")?"video_stats":"log_event";a=v(a);var n=a.next();for(g={};!n.done;g={Kc:void 0,batchRequest:void 0,dangerousLogToVisitorSession:void 0,Nc:void 0,Mc:void 0},n=a.next()){var p=v(n.value);n=p.next().value;p=p.next().value;g.batchRequest=vb({context:cp(b.config_||bp())});if(!Qa(p)&&!S("throw_err_when_logevent_malformed_killswitch")){d();break}g.batchRequest.events=p;(p=qs[n])&&
Hs(g.batchRequest,n,p);delete qs[n];g.dangerousLogToVisitorSession="visitorOnlyApprovedKey"===n;Is(g.batchRequest,h,g.dangerousLogToVisitorSession);S("always_send_and_write")&&(e.writeThenSend=!1);g.Nc=function(r){S("start_client_gcf")&&vi.pa(function(){return A(function(t){return t.yield(Js(r),0)})});
k--;k||c()};
g.Kc=0;g.Mc=function(r){return function(){r.Kc++;if(e.bypassNetworkless&&1===r.Kc)try{Vp(b,l,r.batchRequest,Ks({writeThenSend:!0},r.dangerousLogToVisitorSession,r.Nc,r.Mc,f)),ps=!1}catch(t){Zk(t),d()}k--;k||c()}}(g);
try{Vp(b,l,g.batchRequest,Ks(e,g.dangerousLogToVisitorSession,g.Nc,g.Mc,f)),ps=!1}catch(r){Zk(r),d()}}}
function Ks(a,b,c,d,e){a={retry:!0,onSuccess:c,onError:d,networklessOptions:a,dangerousLogToVisitorSession:b,Uf:!!e,headers:{},postBodyFormat:"",postBody:"",compress:S("compress_gel")||S("compress_gel_lr")};Ls()&&(a.headers["X-Goog-Request-Time"]=JSON.stringify(Math.round(W())));return a}
function Is(a,b,c){Ls()||(a.requestTimeMs=String(b));S("unsplit_gel_payloads_in_logs")&&(a.unsplitGelPayloadsInLogs=!0);!c&&(b=R("EVENT_ID"))&&((c=R("BATCH_CLIENT_COUNTER")||0)||(c=Math.floor(Math.random()*ds/2)),c++,c>ds&&(c=1),Uk("BATCH_CLIENT_COUNTER",c),a.serializedClientEventId={serializedEventId:b,clientCounter:String(c)})}
function Hs(a,b,c){if(c.videoId)var d="VIDEO";else if(c.playlistId)d="PLAYLIST";else return;a.credentialTransferTokenTargetId=c;a.context=a.context||{};a.context.user=a.context.user||{};a.context.user.credentialTransferTokens=[{token:b,scope:d}]}
function us(){var a;(a=E("yt.logging.transport.enableScrapingForTest"))||(a=rl("il_payload_scraping"),a="enable_il_payload_scraping"!==(void 0!==a?String(a):""));a||(Wr=[],D("yt.logging.transport.enableScrapingForTest",!0),D("yt.logging.transport.scrapedPayloadsForTesting",Wr),D("yt.logging.transport.payloadToScrape","visualElementShown visualElementHidden visualElementAttached screenCreated visualElementGestured visualElementStateChanged".split(" ")),D("yt.logging.transport.getScrapedPayloadFromClientEventsFunction"),
D("yt.logging.transport.scrapeClientEvent",!0))}
function Ls(){return S("use_request_time_ms_header")||S("lr_use_request_time_ms_header")}
function Cs(a,b){return!1===S("embeds_transport_use_scheduler")?pl(a,b):S("logging_avoid_blocking_during_navigation")||S("lr_logging_avoid_blocking_during_navigation")?um(function(){if("none"===Vr().currentState)a();else{var c={};Vr().install((c.none={callback:a},c))}},b):um(a,b)}
function Fs(a){S("transport_use_scheduler")?vi.qa(a):window.clearTimeout(a)}
function Js(a){var b,c,d,e,f,g,h,k,l,n;return A(function(p){return 1==p.h?(d=null==(b=a)?void 0:null==(c=b.responseContext)?void 0:c.globalConfigGroup,e=as(d,zk),g=null==(f=d)?void 0:f.hotHashData,h=as(d,yk),l=null==(k=d)?void 0:k.coldHashData,(n=Er().resolve(new yr(Wo)))?g?e?p.yield(Yo(n,g,e),2):p.yield(Yo(n,g),2):p.B(2):p.return()):l?h?p.yield(Zo(n,l,h),0):p.yield(Zo(n,l),0):p.B(0)})}
function Bs(a,b){b=void 0===b?200:b;return a?300===b?ms:ks:300===b?ls:js}
function ws(a){a=Object.keys(a);a=v(a);for(var b=a.next();!b.done;b=a.next())if(b=b.value,qq[b])return b}
function xs(a){switch(a){case "DELAYED_EVENT_TIER_UNSPECIFIED":return 0;case "DELAYED_EVENT_TIER_DEFAULT":return 100;case "DELAYED_EVENT_TIER_DISPATCH_TO_EMPTY":return 200;case "DELAYED_EVENT_TIER_FAST":return 300;case "DELAYED_EVENT_TIER_IMMEDIATE":return 400;default:return 200}}
;var Ms=C.ytLoggingGelSequenceIdObj_||{};D("ytLoggingGelSequenceIdObj_",Ms);
function Ns(a,b,c,d){d=void 0===d?{}:d;var e={},f=Math.round(d.timestamp||W());e.eventTimeMs=f<Number.MAX_SAFE_INTEGER?f:0;e[a]=b;a=ir();e.context={lastActivityMs:String(d.timestamp||!isFinite(a)?-1:a)};d.sequenceGroup&&!S("web_gel_sequence_info_killswitch")&&(a=e.context,b=d.sequenceGroup,Ms[b]=b in Ms?Ms[b]+1:0,a.sequence={index:Ms[b],groupKey:b},d.endOfSequence&&delete Ms[d.sequenceGroup]);(d.sendIsolatedPayload?ys:ts)({endpoint:"log_event",payload:e,cttAuthInfo:d.cttAuthInfo,dangerousLogToVisitorSession:d.dangerousLogToVisitorSession},
c)}
;function ln(a,b,c){c=void 0===c?{}:c;var d=Tq;R("ytLoggingEventsDefaultDisabled",!1)&&Tq===Tq&&(d=null);S("web_all_payloads_via_jspb")&&!c.timestamp&&(c.lact=ir(),c.timestamp=W());Ns(a,b,d,c)}
;D("ytLoggingGelSequenceIdObj_",C.ytLoggingGelSequenceIdObj_||{});var Os=new Set,Ps=0,Qs=0,Rs=0,Ss=[],Ts=["PhantomJS","Googlebot","TO STOP THIS SECURITY SCAN go/scan"];function kn(a){Us(a)}
function Vs(a){Us(a,"WARNING")}
function Ws(a){a instanceof Error?Us(a):(a=Ra(a)?JSON.stringify(a):String(a),a=new V(a),a.name="RejectedPromiseError",Vs(a))}
function Us(a,b,c,d,e,f,g,h){f=void 0===f?{}:f;f.name=c||R("INNERTUBE_CONTEXT_CLIENT_NAME",1);f.version=d||R("INNERTUBE_CONTEXT_CLIENT_VERSION");c=f;b=void 0===b?"ERROR":b;g=void 0===g?!1:g;b=void 0===b?"ERROR":b;g=void 0===g?!1:g;if(a&&(a.hasOwnProperty("level")&&a.level&&(b=a.level),S("console_log_js_exceptions")&&(d=[],d.push("Name: "+a.name),d.push("Message: "+a.message),a.hasOwnProperty("params")&&d.push("Error Params: "+JSON.stringify(a.params)),a.hasOwnProperty("args")&&d.push("Error args: "+
JSON.stringify(a.args)),d.push("File name: "+a.fileName),d.push("Stacktrace: "+a.stack),d=d.join("\n"),window.console.log(d,a)),!(5<=Ps))){d=Ss;var k=vc(a);e=k.message||"Unknown Error";f=k.name||"UnknownError";var l=k.stack||a.i||"Not available";if(l.startsWith(f+": "+e)){var n=l.split("\n");n.shift();l=n.join("\n")}n=k.lineNumber||"Not available";k=k.fileName||"Not available";var p=0;if(a.hasOwnProperty("args")&&a.args&&a.args.length)for(var r=0;r<a.args.length&&!(p=Sl(a.args[r],"params."+r,c,p),
500<=p);r++);else if(a.hasOwnProperty("params")&&a.params){var t=a.params;if("object"===typeof a.params)for(r in t){if(t[r]){var x="params."+r,z=Ul(t[r]);c[x]=z;p+=x.length+z.length;if(500<p)break}}else c.params=Ul(t)}if(d.length)for(r=0;r<d.length&&!(p=Sl(d[r],"params.context."+r,c,p),500<=p);r++);navigator.vendor&&!c.hasOwnProperty("vendor")&&(c["device.vendor"]=navigator.vendor);r={message:e,name:f,lineNumber:n,fileName:k,stack:l,params:c,sampleWeight:1};c=Number(a.columnNumber);isNaN(c)||(r.lineNumber=
r.lineNumber+":"+c);if("IGNORED"===a.level)a=0;else a:{a=Ol();c=v(a.Ta);for(d=c.next();!d.done;d=c.next())if(d=d.value,r.message&&r.message.match(d.fg)){a=d.weight;break a}a=v(a.Qa);for(c=a.next();!c.done;c=a.next())if(c=c.value,c.callback(r)){a=c.weight;break a}a=1}r.sampleWeight=a;a=v(Jl);for(c=a.next();!c.done;c=a.next())if(c=c.value,c.fc[r.name])for(e=v(c.fc[r.name]),d=e.next();!d.done;d=e.next())if(f=d.value,d=r.message.match(f.regexp)){r.params["params.error.original"]=d[0];e=f.groups;f={};
for(n=0;n<e.length;n++)f[e[n]]=d[n+1],r.params["params.error."+e[n]]=d[n+1];r.message=c.Ic(f);break}r.params||(r.params={});a=Ol();r.params["params.errorServiceSignature"]="msg="+a.Ta.length+"&cb="+a.Qa.length;r.params["params.serviceWorker"]="false";C.document&&C.document.querySelectorAll&&(r.params["params.fscripts"]=String(document.querySelectorAll("script:not([nonce])").length));Cb("sample").constructor!==Ab&&(r.params["params.fconst"]="true");window.yterr&&"function"===typeof window.yterr&&window.yterr(r);
if(0!==r.sampleWeight&&!Os.has(r.message)){if(g&&S("web_enable_error_204"))Xs(void 0===b?"ERROR":b,r);else{b=void 0===b?"ERROR":b;"ERROR"===b?(Pl.Ya("handleError",r),S("record_app_crashed_web")&&0===Rs&&1===r.sampleWeight&&(Rs++,g={appCrashType:"APP_CRASH_TYPE_BREAKPAD"},S("report_client_error_with_app_crash_ks")||(g.systemHealth={crashData:{clientError:{logMessage:{message:r.message}}}}),ln("appCrashed",g)),Qs++):"WARNING"===b&&Pl.Ya("handleWarning",r);if(S("kevlar_gel_error_routing")){g=b;h=void 0===
h?{}:h;b:{a=v(Ts);for(c=a.next();!c.done;c=a.next())if(rn(c.value.toLowerCase())){a=!0;break b}a=!1}if(a)h=void 0;else{c={stackTrace:r.stack};r.fileName&&(c.filename=r.fileName);a=r.lineNumber&&r.lineNumber.split?r.lineNumber.split(":"):[];0!==a.length&&(1!==a.length||isNaN(Number(a[0]))?2!==a.length||isNaN(Number(a[0]))||isNaN(Number(a[1]))||(c.lineNumber=Number(a[0]),c.columnNumber=Number(a[1])):c.lineNumber=Number(a[0]));a={level:"ERROR_LEVEL_UNKNOWN",message:r.message,errorClassName:r.name,sampleWeight:r.sampleWeight};
"ERROR"===g?a.level="ERROR_LEVEL_ERROR":"WARNING"===g&&(a.level="ERROR_LEVEL_WARNNING");c={isObfuscated:!0,browserStackInfo:c};h.pageUrl=window.location.href;h.kvPairs=[];R("FEXP_EXPERIMENTS")&&(h.experimentIds=R("FEXP_EXPERIMENTS"));d=R("LATEST_ECATCHER_SERVICE_TRACKING_PARAMS");if(!Vk("web_disable_gel_stp_ecatcher_killswitch")&&d)for(e=v(Object.keys(d)),f=e.next();!f.done;f=e.next())f=f.value,h.kvPairs.push({key:f,value:String(d[f])});if(d=r.params)for(e=v(Object.keys(d)),f=e.next();!f.done;f=e.next())f=
f.value,h.kvPairs.push({key:"client."+f,value:String(d[f])});d=R("SERVER_NAME");e=R("SERVER_VERSION");d&&e&&(h.kvPairs.push({key:"server.name",value:d}),h.kvPairs.push({key:"server.version",value:e}));h={errorMetadata:h,stackTrace:c,logMessage:a}}h&&(ln("clientError",h),("ERROR"===g||S("errors_flush_gel_always_killswitch"))&&As(void 0,void 0,!1))}S("suppress_error_204_logging")||Xs(b,r)}try{Os.add(r.message)}catch(y){}Ps++}}}
function Xs(a,b){var c=b.params||{};a={urlParams:{a:"logerror",t:"jserror",type:b.name,msg:b.message.substr(0,250),line:b.lineNumber,level:a,"client.name":c.name},postParams:{url:R("PAGE_NAME",window.location.href),file:b.fileName},method:"POST"};c.version&&(a["client.version"]=c.version);if(a.postParams){b.stack&&(a.postParams.stack=b.stack);b=v(Object.keys(c));for(var d=b.next();!d.done;d=b.next())d=d.value,a.postParams["client."+d]=c[d];if(c=R("LATEST_ECATCHER_SERVICE_TRACKING_PARAMS"))for(b=v(Object.keys(c)),
d=b.next();!d.done;d=b.next())d=d.value,a.postParams[d]=c[d];c=R("SERVER_NAME");b=R("SERVER_VERSION");c&&b&&(a.postParams["server.name"]=c,a.postParams["server.version"]=b)}Al(R("ECATCHER_REPORT_HOST","")+"/error_204",a)}
;function Ys(){this.register=new Map}
function Zs(a){a=v(a.register.values());for(var b=a.next();!b.done;b=a.next())b.value.jg("ABORTED")}
Ys.prototype.clear=function(){Zs(this);this.register.clear()};
var $s=new Ys;var at=Date.now().toString();function bt(){for(var a=Array(16),b=0;16>b;b++){for(var c=Date.now(),d=0;d<c%23;d++)a[b]=Math.random();a[b]=Math.floor(256*Math.random())}if(at)for(b=1,c=0;c<at.length;c++)a[b%16]=a[b%16]^a[(b-1)%16]/4^at.charCodeAt(c),b++;return a}
function ct(){a:{if(window.crypto&&window.crypto.getRandomValues)try{var a=Array(16),b=new Uint8Array(16);window.crypto.getRandomValues(b);for(var c=0;c<a.length;c++)a[c]=b[c];var d=a;break a}catch(e){}d=bt()}a=[];for(b=0;b<d.length;b++)a.push("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_".charAt(d[b]&63));return a.join("")}
;var dt,et=C.ytLoggingDocDocumentNonce_;et||(et=ct(),D("ytLoggingDocDocumentNonce_",et));dt=et;function ft(a){this.h=a}
m=ft.prototype;m.getAsJson=function(){var a={};void 0!==this.h.trackingParams?a.trackingParams=this.h.trackingParams:(a.veType=this.h.veType,void 0!==this.h.veCounter&&(a.veCounter=this.h.veCounter),void 0!==this.h.elementIndex&&(a.elementIndex=this.h.elementIndex));void 0!==this.h.dataElement&&(a.dataElement=this.h.dataElement.getAsJson());void 0!==this.h.youtubeData&&(a.youtubeData=this.h.youtubeData);this.h.isCounterfactual&&(a.isCounterfactual=!0);return a};
m.getAsJspb=function(){var a=new Gk;void 0!==this.h.trackingParams?a.setTrackingParams(this.h.trackingParams):(void 0!==this.h.veType&&Of(a,2,rf(this.h.veType)),void 0!==this.h.veCounter&&Of(a,6,rf(this.h.veCounter)),void 0!==this.h.elementIndex&&Of(a,3,rf(this.h.elementIndex)),this.h.isCounterfactual&&Of(a,5,of(!0)));if(void 0!==this.h.dataElement){var b=this.h.dataElement.getAsJspb();Wf(a,Gk,7,b)}void 0!==this.h.youtubeData&&Wf(a,Ak,8,this.h.jspbYoutubeData);return a};
m.toString=function(){return JSON.stringify(this.getAsJson())};
m.isClientVe=function(){return!this.h.trackingParams&&!!this.h.veType};
m.getLoggingDirectives=function(){return this.h.loggingDirectives};function gt(a){return R("client-screen-nonce-store",{})[void 0===a?0:a]}
function ht(a,b){b=void 0===b?0:b;var c=R("client-screen-nonce-store");c||(c={},Uk("client-screen-nonce-store",c));c[b]=a}
function jt(a){a=void 0===a?0:a;return 0===a?"ROOT_VE_TYPE":"ROOT_VE_TYPE."+a}
function kt(a){return R(jt(void 0===a?0:a))}
D("yt_logging_screen.getRootVeType",kt);function lt(){var a=R("csn-to-ctt-auth-info");a||(a={},Uk("csn-to-ctt-auth-info",a));return a}
function mt(){return Object.values(R("client-screen-nonce-store",{})).filter(function(a){return void 0!==a})}
function nt(a){a=gt(void 0===a?0:a);if(!a&&!R("USE_CSN_FALLBACK",!0))return null;a||(a="UNDEFINED_CSN");return a?a:null}
D("yt_logging_screen.getCurrentCsn",nt);function ot(a,b,c){var d=lt();(c=nt(c))&&delete d[c];b&&(d[a]=b)}
function pt(a){return lt()[a]}
D("yt_logging_screen.getCttAuthInfo",pt);D("yt_logging_screen.setCurrentScreen",function(a,b,c,d){c=void 0===c?0:c;if(a!==gt(c)||b!==R(jt(c)))if(ot(a,d,c),ht(a,c),Uk(jt(c),b),b=function(){setTimeout(function(){a&&ln("foregroundHeartbeatScreenAssociated",{clientDocumentNonce:dt,clientScreenNonce:a})},0)},"requestAnimationFrame"in window)try{window.requestAnimationFrame(b)}catch(e){b()}else b()});function qt(){var a=ub(rt),b;return(new Kd(function(c,d){a.onSuccess=function(e){ol(e)?c(new st(e)):d(new tt("Request failed, status="+(e&&"status"in e?e.status:-1),"net.badstatus",e))};
a.onError=function(e){d(new tt("Unknown request error","net.unknown",e))};
a.onTimeout=function(e){d(new tt("Request timed out","net.timeout",e))};
b=Al("//googleads.g.doubleclick.net/pagead/id",a)})).nc(function(c){if(c instanceof Rd){var d;
null==(d=b)||d.abort()}return Pd(c)})}
function tt(a,b,c){bb.call(this,a+", errorCode="+b);this.errorCode=b;this.xhr=c;this.name="PromiseAjaxError"}
w(tt,bb);function st(a){this.xhr=a}
;function ut(){this.h=0;this.i=null}
ut.prototype.then=function(a,b,c){return 1===this.h&&a?(a=a.call(c,this.i))&&"function"===typeof a.then?a:vt(a):2===this.h&&b?(a=b.call(c,this.i))&&"function"===typeof a.then?a:wt(a):this};
ut.prototype.getValue=function(){return this.i};
ut.prototype.isRejected=function(){return 2==this.h};
ut.prototype.$goog_Thenable=!0;function wt(a){var b=new ut;a=void 0===a?null:a;b.h=2;b.i=void 0===a?null:a;return b}
function vt(a){var b=new ut;a=void 0===a?null:a;b.h=1;b.i=void 0===a?null:a;return b}
;function xt(a,b){var c=void 0===c?{}:c;a={method:void 0===b?"POST":b,mode:jl(a)?"same-origin":"cors",credentials:jl(a)?"same-origin":"include"};b={};for(var d=v(Object.keys(c)),e=d.next();!e.done;e=d.next())e=e.value,c[e]&&(b[e]=c[e]);0<Object.keys(b).length&&(a.headers=b);return a}
;function zt(){return wg()||(re||se)&&rn("applewebkit")&&!rn("version")&&(!rn("safari")||rn("gsa/"))||Ic&&rn("version/")?!0:R("EOM_VISITOR_DATA")?!1:!0}
;function At(a){a:{var b="EMBEDDED_PLAYER_MODE_UNKNOWN";window.location.hostname.includes("youtubeeducation.com")&&(b="EMBEDDED_PLAYER_MODE_PFL");var c=a.raw_embedded_player_response;if(!c&&(a=a.embedded_player_response))try{c=JSON.parse(a)}catch(e){break a}if(c)b:for(var d in Ek)if(Ek[d]==c.embeddedPlayerMode){b=Ek[d];break b}}return"EMBEDDED_PLAYER_MODE_PFL"===b}
;function Bt(a){bb.call(this,a.message||a.description||a.name);this.isMissing=a instanceof Ct;this.isTimeout=a instanceof tt&&"net.timeout"==a.errorCode;this.isCanceled=a instanceof Rd}
w(Bt,bb);Bt.prototype.name="BiscottiError";function Ct(){bb.call(this,"Biscotti ID is missing from server")}
w(Ct,bb);Ct.prototype.name="BiscottiMissingError";var rt={format:"RAW",method:"GET",timeout:5E3,withCredentials:!0},Dt=null;function Et(){if(S("disable_biscotti_fetch_entirely_for_all_web_clients"))return Error("Biscotti id fetching has been disabled entirely.");if(!zt())return Error("User has not consented - not fetching biscotti id.");var a=R("PLAYER_VARS",{});if("1"==sb(a))return Error("Biscotti ID is not available in private embed mode");if(At(a))return Error("Biscotti id fetching has been disabled for pfl.")}
function Nk(){var a=Et();if(void 0!==a)return Pd(a);Dt||(Dt=qt().then(Ft).nc(function(b){return Gt(2,b)}));
return Dt}
function Ft(a){a=a.xhr.responseText;if(0!=a.lastIndexOf(")]}'",0))throw new Ct;a=JSON.parse(a.substr(4));if(1<(a.type||1))throw new Ct;a=a.id;Ok(a);Dt=vt(a);Ht(18E5,2);return a}
function Gt(a,b){b=new Bt(b);Ok("");Dt=wt(b);0<a&&Ht(12E4,a-1);throw b;}
function Ht(a,b){pl(function(){qt().then(Ft,function(c){return Gt(b,c)}).nc(db)},a)}
function It(){try{var a=E("yt.ads.biscotti.getId_");return a?a():Nk()}catch(b){return Pd(b)}}
;var bi=ka(["data-"]);function Jt(a){a&&(a.dataset?a.dataset[Kt()]="true":ai(a))}
function Lt(a){return a?a.dataset?a.dataset[Kt()]:a.getAttribute("data-loaded"):null}
var Mt={};function Kt(){return Mt.loaded||(Mt.loaded="loaded".replace(/\-([a-z])/g,function(a,b){return b.toUpperCase()}))}
;function Nt(a,b,c){H.call(this);var d=this;c=c||R("POST_MESSAGE_ORIGIN")||window.document.location.protocol+"//"+window.document.location.hostname;this.i=b||null;this.targetOrigin="*";this.j=c;this.sessionId=null;this.channel="widget";this.D=!!a;this.A=function(e){a:if(!("*"!=d.j&&e.origin!=d.j||d.i&&e.source!=d.i||"string"!==typeof e.data)){try{var f=JSON.parse(e.data)}catch(g){break a}if(!(null==f||d.D&&(d.sessionId&&d.sessionId!=f.id||d.channel&&d.channel!=f.channel))&&f)switch(f.event){case "listening":"null"!=
e.origin&&(d.j=d.targetOrigin=e.origin);d.i=e.source;d.sessionId=f.id;d.h&&(d.h(),d.h=null);break;case "command":d.l&&(!d.m||0<=fb(d.m,f.func))&&d.l(f.func,f.args,e.origin)}}};
this.m=this.h=this.l=null;window.addEventListener("message",this.A)}
w(Nt,H);Nt.prototype.sendMessage=function(a,b){if(b=b||this.i){this.sessionId&&(a.id=this.sessionId);this.channel&&(a.channel=this.channel);try{var c=JSON.stringify(a);b.postMessage(c,this.targetOrigin)}catch(d){$k(d)}}};
Nt.prototype.R=function(){window.removeEventListener("message",this.A);H.prototype.R.call(this)};function Ot(a){a=a||{};var b={},c={};this.url=a.url||"";this.args=a.args||ub(b);this.assets=a.assets||{};this.attrs=a.attrs||ub(c);this.fallback=a.fallback||null;this.fallbackMessage=a.fallbackMessage||null;this.html5=!!a.html5;this.disable=a.disable||{};this.loaded=!!a.loaded;this.messages=a.messages||{}}
Ot.prototype.clone=function(){var a=new Ot,b;for(b in this)if(this.hasOwnProperty(b)){var c=this[b];"object"==Pa(c)?a[b]=ub(c):a[b]=c}return a};var Pt=["share/get_web_player_share_panel"],Qt=["feedback"],Rt=["notification/modify_channel_preference"],St=["browse/edit_playlist"],Tt=["subscription/subscribe"],Ut=["subscription/unsubscribe"];var Vt=window.yt&&window.yt.msgs_||window.ytcfg&&window.ytcfg.msgs||{};D("yt.msgs_",Vt);function Wt(a){Pk(Vt,arguments)}
;var Xt=/\.vflset|-vfl[a-zA-Z0-9_+=-]+/,Yt=/-[a-zA-Z]{2,3}_[a-zA-Z]{2,3}(?=(\/|$))/;function Zt(a,b,c){c=void 0===c?null:c;if(S("web_simple_scriptloader"))$t(a,b,c);else if(window.spf&&spf.script){c="";if(a){var d=a.indexOf("jsbin/"),e=a.lastIndexOf(".js"),f=d+6;-1<d&&-1<e&&e>f&&(c=a.substring(f,e),c=c.replace(Xt,""),c=c.replace(Yt,""),c=c.replace("debug-",""),c=c.replace("tracing-",""))}spf.script.load(a,c,b)}else $t(a,b,c)}
function $t(a,b,c){c=void 0===c?null:c;var d=au(a),e=document.getElementById(d),f=e&&Lt(e),g=e&&!f;f?b&&b():(b&&(f=nr(d,b),b=""+Sa(b),bu[b]=f),g||(e=cu(a,d,function(){Lt(e)||(Jt(e),tr(d),pl(function(){ur(d)},0))},c)))}
function cu(a,b,c,d){d=void 0===d?null:d;var e=wd("SCRIPT");e.id=b;e.onload=function(){c&&setTimeout(c,0)};
e.onreadystatechange=function(){switch(e.readyState){case "loaded":case "complete":e.onload()}};
d&&e.setAttribute("nonce",d);ii(e,wk(a));a=document.getElementsByTagName("head")[0]||document.body;a.insertBefore(e,a.firstChild);return e}
function du(a){a=au(a);var b=document.getElementById(a);b&&(ur(a),b.parentNode.removeChild(b))}
function eu(a,b){a&&b&&(a=""+Sa(b),(a=bu[a])&&pr(a))}
function au(a){var b=document.createElement("a");Yh(b,a);a=b.href.replace(/^[a-zA-Z]+:\/\//,"//");return"js-"+Zb(a)}
var bu={};var fu=/cssbin\/(?:debug-)?([a-zA-Z0-9_-]+?)(?:-2x|-web|-rtl|-vfl|.css)/;function gu(a){a=a||"";if(S("web_simple_styleloader"))hu(a);else if(window.spf){var b=a.match(fu);spf.style.load(a,b?b[1]:"",void 0)}else hu(a)}
function hu(a){var b=iu(a),c=document.getElementById(b),d=c&&Lt(c);d||c&&!d||(c=ju(a,b,function(){if(!Lt(c)){Jt(c);tr(b);var e=Ya(ur,b);pl(e,0)}}))}
function ju(a,b,c){var d=document.createElement("link");d.id=b;d.onload=function(){c&&setTimeout(c,0)};
a=wk(a);ei(d,a);(document.getElementsByTagName("head")[0]||document.body).appendChild(d);return d}
function iu(a){var b=wd("A");Yh(b,new Hb(a,Ib));a=b.href.replace(/^[a-zA-Z]+:\/\//,"//");return"css-"+Zb(a)}
;function ku(a){var b=B.apply(1,arguments);if(!lu(a)||b.some(function(d){return!lu(d)}))throw Error("Only objects may be merged.");
b=v(b);for(var c=b.next();!c.done;c=b.next())mu(a,c.value)}
function mu(a,b){for(var c in b)if(lu(b[c])){if(c in a&&!lu(a[c]))throw Error("Cannot merge an object into a non-object.");c in a||(a[c]={});mu(a[c],b[c])}else if(nu(b[c])){if(c in a&&!nu(a[c]))throw Error("Cannot merge an array into a non-array.");c in a||(a[c]=[]);ou(a[c],b[c])}else a[c]=b[c];return a}
function ou(a,b){b=v(b);for(var c=b.next();!c.done;c=b.next())c=c.value,lu(c)?a.push(mu({},c)):nu(c)?a.push(ou([],c)):a.push(c);return a}
function lu(a){return"object"===typeof a&&!Array.isArray(a)}
function nu(a){return"object"===typeof a&&Array.isArray(a)}
;function pu(a){a=void 0===a?!1:a;H.call(this);this.h=new L(a);tc(this,this.h)}
$a(pu,H);pu.prototype.subscribe=function(a,b,c){return this.Z()?0:this.h.subscribe(a,b,c)};
pu.prototype.unsubscribe=function(a,b,c){return this.Z()?!1:this.h.unsubscribe(a,b,c)};
pu.prototype.l=function(a,b){this.Z()||this.h.Ya.apply(this.h,arguments)};var qu="absolute_experiments app conditional_experiments debugcss debugjs expflag forced_experiments pbj pbjreload sbb spf spfreload sr_bns_address sttick".split(" ");
function ru(a,b){var c=void 0===c?!0:c;var d=R("VALID_SESSION_TEMPDATA_DOMAINS",[]),e=cc(window.location.href);e&&d.push(e);e=cc(a);if(0<=fb(d,e)||!e&&0==a.lastIndexOf("/",0))if(d=document.createElement("a"),Yh(d,a),a=d.href)if(a=dc(a),a=ec(a))if(c&&!b.csn&&(b.itct||b.ved)&&(b=Object.assign({csn:nt()},b)),f){var f=parseInt(f,10);isFinite(f)&&0<f&&su(a,b,f)}else su(a,b)}
function su(a,b,c){a=tu(a);b=b?hc(b):"";c=c||5;zt()&&am(a,b,c)}
function tu(a){for(var b=v(qu),c=b.next();!c.done;c=b.next())a=mc(a,c.value);return"ST-"+Zb(a).toString(36)}
;function uu(a){gp.call(this,1,arguments);this.csn=a}
w(uu,gp);var pp=new hp("screen-created",uu),vu=[],wu=0,xu=new Map,yu=new Map,zu=new Map;
function Au(a,b,c,d,e){e=void 0===e?!1:e;if(!S("do_not_send_empty_attach_payloads")||d&&!(1>d.length)){for(var f=Bu({cttAuthInfo:pt(b)||void 0},b),g=v(d),h=g.next();!h.done;h=g.next()){h=h.value;var k=h.getAsJson();(qb(k)||!k.trackingParams&&!k.veType)&&Vs(Error("Child VE logged with no data"));if(S("no_client_ve_attach_unless_shown")){var l=Cu(h,b);if(k.veType&&!yu.has(l)&&!zu.has(l)&&!e){if(!S("il_attach_cache_limit")||1E3>xu.size){xu.set(l,[a,b,c,h]);return}S("il_attach_cache_limit")&&1E3<xu.size&&
Vs(new V("IL Attach cache exceeded limit"))}h=Cu(c,b);xu.has(h)?Du(c,b):zu.set(h,!0)}}d=d.filter(function(n){n.csn!==b?(n.csn=b,n=!0):n=!1;return n});
c={csn:b,parentVe:c.getAsJson(),childVes:ib(d,function(n){return n.getAsJson()})};
"UNDEFINED_CSN"===b?Eu("visualElementAttached",f,c):a?Ns("visualElementAttached",c,a,f):ln("visualElementAttached",c,f)}}
function Eu(a,b,c){vu.push({Ee:a,payload:c,ag:void 0,options:b});wu||(wu=qp())}
function rp(a){if(vu){for(var b=v(vu),c=b.next();!c.done;c=b.next())c=c.value,c.payload&&(c.payload.csn=a.csn,ln(c.Ee,c.payload,c.options));vu.length=0}wu=0}
function Cu(a,b){return""+a.getAsJson().veType+a.getAsJson().veCounter+b}
function Du(a,b){a=Cu(a,b);xu.has(a)&&(b=xu.get(a)||[],Au(b[0],b[1],b[2],[b[3]],!0),xu.delete(a))}
function Bu(a,b){S("log_sequence_info_on_gel_web")&&(a.sequenceGroup=b);return a}
;function Fu(){try{return!!self.localStorage}catch(a){return!1}}
;function Gu(a){a=a.match(/(.*)::.*::.*/);if(null!==a)return a[1]}
function Hu(a){if(Fu()){var b=Object.keys(window.localStorage);b=v(b);for(var c=b.next();!c.done;c=b.next()){c=c.value;var d=Gu(c);void 0===d||a.includes(d)||self.localStorage.removeItem(c)}}}
function Iu(){if(!Fu())return!1;var a=sm(),b=Object.keys(window.localStorage);b=v(b);for(var c=b.next();!c.done;c=b.next())if(c=Gu(c.value),void 0!==c&&c!==a)return!0;return!1}
;function Ju(){var a=!1;try{a=!!window.sessionStorage.getItem("session_logininfo")}catch(b){a=!0}return S("copy_login_info_to_st_cookie")&&("WEB"===R("INNERTUBE_CLIENT_NAME")||"WEB_CREATOR"===R("INNERTUBE_CLIENT_NAME"))&&a}
function Ku(a){if(R("LOGGED_IN",!0)&&Ju()){var b=R("VALID_SESSION_TEMPDATA_DOMAINS",[]);var c=cc(window.location.href);c&&b.push(c);c=cc(a);0<=fb(b,c)||!c&&0==a.lastIndexOf("/",0)?(b=dc(a),(b=ec(b))?(b=tu(b),b=(b=bm(b)||null)?gl(b):{}):b=null):b=null;null==b&&(b={});c=b;var d=void 0;Ju()?(d||(d=R("LOGIN_INFO")),d?(c.session_logininfo=d,c=!0):c=!1):c=!1;c&&ru(a,b)}}
;function Lu(a,b,c){b=void 0===b?{}:b;c=void 0===c?!1:c;var d=R("EVENT_ID");d&&(b.ei||(b.ei=d));b&&ru(a,b);if(c)return!1;Ku(a);var e=void 0===e?{}:e;var f=void 0===f?"":f;var g=void 0===g?window:g;a=ic(a,e);Ku(a);f=a+f;var h=void 0===h?Vh:h;a:if(h=void 0===h?Vh:h,f instanceof Hb)h=f;else{for(a=0;a<h.length;++a)if(b=h[a],b instanceof Th&&b.te(f)){h=new Hb(f,Ib);break a}h=void 0}g=g.location;h=Xh(h||Yb);void 0!==h&&(g.href=h);return!0}
;function Mu(a){if("1"!=sb(R("PLAYER_VARS",{}))){a&&Mk();try{It().then(function(){},function(){}),pl(Mu,18E5)}catch(b){Zk(b)}}}
;var Nu=new Map([["dark","USER_INTERFACE_THEME_DARK"],["light","USER_INTERFACE_THEME_LIGHT"]]);function Ou(){var a=void 0===a?window.location.href:a;if(S("kevlar_disable_theme_param"))return null;ac(bc(5,a));try{var b=hl(a).theme;return Nu.get(b)||null}catch(c){}return null}
;function Pu(){this.h={};if(this.i=dm()){var a=bm("CONSISTENCY");a&&Qu(this,{encryptedTokenJarContents:a})}}
Pu.prototype.handleResponse=function(a,b){if(!b)throw Error("request needs to be passed into ConsistencyService");var c,d;b=(null==(c=b.Ma.context)?void 0:null==(d=c.request)?void 0:d.consistencyTokenJars)||[];var e;if(a=null==(e=a.responseContext)?void 0:e.consistencyTokenJar){e=v(b);for(c=e.next();!c.done;c=e.next())delete this.h[c.value.encryptedTokenJarContents];Qu(this,a)}};
function Qu(a,b){if(b.encryptedTokenJarContents&&(a.h[b.encryptedTokenJarContents]=b,"string"===typeof b.expirationSeconds)){var c=Number(b.expirationSeconds);setTimeout(function(){delete a.h[b.encryptedTokenJarContents]},1E3*c);
a.i&&am("CONSISTENCY",b.encryptedTokenJarContents,c,void 0,!0)}}
;var Ru=window.location.hostname.split(".").slice(-2).join(".");function Su(){var a=R("LOCATION_PLAYABILITY_TOKEN");"TVHTML5"===R("INNERTUBE_CLIENT_NAME")&&(this.h=Tu(this))&&(a=this.h.get("yt-location-playability-token"));a&&(this.locationPlayabilityToken=a,this.i=void 0)}
var Uu;function Vu(){Uu=E("yt.clientLocationService.instance");Uu||(Uu=new Su,D("yt.clientLocationService.instance",Uu));return Uu}
m=Su.prototype;m.setLocationOnInnerTubeContext=function(a){a.client||(a.client={});this.i?(a.client.locationInfo||(a.client.locationInfo={}),a.client.locationInfo.latitudeE7=Math.floor(1E7*this.i.coords.latitude),a.client.locationInfo.longitudeE7=Math.floor(1E7*this.i.coords.longitude),a.client.locationInfo.horizontalAccuracyMeters=Math.round(this.i.coords.accuracy),a.client.locationInfo.forceLocationPlayabilityTokenRefresh=!0):this.locationPlayabilityToken&&(a.client.locationPlayabilityToken=this.locationPlayabilityToken)};
m.handleResponse=function(a){var b;a=null==(b=a.responseContext)?void 0:b.locationPlayabilityToken;void 0!==a&&(this.locationPlayabilityToken=a,this.i=void 0,"TVHTML5"===R("INNERTUBE_CLIENT_NAME")?(this.h=Tu(this))&&this.h.set("yt-location-playability-token",a,15552E3):am("YT_CL",JSON.stringify({loctok:a}),15552E3,Ru,!0))};
function Tu(a){return void 0===a.h?new bn("yt-client-location"):a.h}
m.clearLocationPlayabilityToken=function(a){"TVHTML5"===a?(this.h=Tu(this))&&this.h.remove("yt-location-playability-token"):cm("YT_CL")};
m.getCurrentPositionFromGeolocation=function(){var a=this;if(!(navigator&&navigator.geolocation&&navigator.geolocation.getCurrentPosition))return Promise.reject(Error("Geolocation unsupported"));var b=!1,c=1E4;"MWEB"===R("INNERTUBE_CLIENT_NAME")&&(b=!0,c=15E3);return new Promise(function(d,e){navigator.geolocation.getCurrentPosition(function(f){a.i=f;d(f)},function(f){e(f)},{enableHighAccuracy:b,
maximumAge:0,timeout:c})})};
m.createUnpluggedLocationInfo=function(a){var b={};a=a.coords;if(null==a?0:a.latitude)b.latitudeE7=Math.floor(1E7*a.latitude);if(null==a?0:a.longitude)b.longitudeE7=Math.floor(1E7*a.longitude);if(null==a?0:a.accuracy)b.locationRadiusMeters=Math.round(a.accuracy);return b};
m.createLocationInfo=function(a){var b={};a=a.coords;if(null==a?0:a.latitude)b.latitudeE7=Math.floor(1E7*a.latitude);if(null==a?0:a.longitude)b.longitudeE7=Math.floor(1E7*a.longitude);return b};function Wu(a,b){var c,d=null==(c=as(a,Dk))?void 0:c.signal;if(d&&b.Ob&&(c=b.Ob[d]))return c();var e;if((c=null==(e=as(a,Bk))?void 0:e.request)&&b.Vd&&(e=b.Vd[c]))return e();for(var f in a)if(b.cd[f]&&(a=b.cd[f]))return a()}
function Xu(a){var b={"Content-Type":"application/json"};R("EOM_VISITOR_DATA")?b["X-Goog-EOM-Visitor-Id"]=R("EOM_VISITOR_DATA"):R("VISITOR_DATA")&&(b["X-Goog-Visitor-Id"]=R("VISITOR_DATA"));b["X-Youtube-Bootstrap-Logged-In"]=R("LOGGED_IN",!1);R("DEBUG_SETTINGS_METADATA")&&(b["X-Debug-Settings-Metadata"]=R("DEBUG_SETTINGS_METADATA"));"cors"!==a&&((a=R("INNERTUBE_CONTEXT_CLIENT_NAME"))&&(b["X-Youtube-Client-Name"]=a),(a=R("INNERTUBE_CONTEXT_CLIENT_VERSION"))&&(b["X-Youtube-Client-Version"]=a),(a=R("CHROME_CONNECTED_HEADER"))&&
(b["X-Youtube-Chrome-Connected"]=a),(a=R("DOMAIN_ADMIN_STATE"))&&(b["X-Youtube-Domain-Admin-State"]=a));return b}
;function Yu(a){return function(){return new a}}
;var Zu={},$u=(Zu.WEB_UNPLUGGED="^unplugged/",Zu.WEB_UNPLUGGED_ONBOARDING="^unplugged/",Zu.WEB_UNPLUGGED_OPS="^unplugged/",Zu.WEB_UNPLUGGED_PUBLIC="^unplugged/",Zu.WEB_CREATOR="^creator/",Zu.WEB_KIDS="^kids/",Zu.WEB_EXPERIMENTS="^experiments/",Zu.WEB_MUSIC="^music/",Zu.WEB_REMIX="^music/",Zu.WEB_MUSIC_EMBEDDED_PLAYER="^music/",Zu.WEB_MUSIC_EMBEDDED_PLAYER="^main_app/|^sfv/",Zu);
function av(a){var b=void 0===b?"UNKNOWN_INTERFACE":b;if(1===a.length)return a[0];var c=$u[b];if(c){c=new RegExp(c);for(var d=v(a),e=d.next();!e.done;e=d.next())if(e=e.value,c.exec(e))return e}var f=[];Object.entries($u).forEach(function(g){var h=v(g);g=h.next().value;h=h.next().value;b!==g&&f.push(h)});
c=new RegExp(f.join("|"));a.sort(function(g,h){return g.length-h.length});
d=v(a);for(e=d.next();!e.done;e=d.next())if(e=e.value,!c.exec(e))return e;return a[0]}
;function bv(){}
bv.prototype.v=function(a,b,c){b=void 0===b?{}:b;c=void 0===c?Yl:c;var d=a.clickTrackingParams,e=this.l,f=!1;f=void 0===f?!1:f;e=void 0===e?!1:e;var g=R("INNERTUBE_CONTEXT");if(g){g=vb(g);S("web_no_tracking_params_in_shell_killswitch")||delete g.clickTracking;g.client||(g.client={});var h=g.client;"MWEB"===h.clientName&&"AUTOMOTIVE_FORM_FACTOR"!==h.clientFormFactor&&(h.clientFormFactor=R("IS_TABLET")?"LARGE_FORM_FACTOR":"SMALL_FORM_FACTOR");h.screenWidthPoints=window.innerWidth;h.screenHeightPoints=
window.innerHeight;h.screenPixelDensity=Math.round(window.devicePixelRatio||1);h.screenDensityFloat=window.devicePixelRatio||1;h.utcOffsetMinutes=-Math.floor((new Date).getTimezoneOffset());var k=void 0===k?!1:k;hm();var l="USER_INTERFACE_THEME_LIGHT";km(165)?l="USER_INTERFACE_THEME_DARK":km(174)?l="USER_INTERFACE_THEME_LIGHT":!S("kevlar_legacy_browsers")&&window.matchMedia&&window.matchMedia("(prefers-color-scheme)").matches&&window.matchMedia("(prefers-color-scheme: dark)").matches&&(l="USER_INTERFACE_THEME_DARK");
k=k?l:Ou()||l;h.userInterfaceTheme=k;if(!f){if(k=pm())h.connectionType=k;S("web_log_effective_connection_type")&&(k=qm())&&(g.client.effectiveConnectionType=k)}var n;if(S("web_log_memory_total_kbytes")&&(null==(n=C.navigator)?0:n.deviceMemory)){var p;n=null==(p=C.navigator)?void 0:p.deviceMemory;g.client.memoryTotalKbytes=""+1E6*n}S("web_gcf_hashes_innertube")&&(k=$o())&&(p=k.coldConfigData,n=k.coldHashData,k=k.hotHashData,g.client.configInfo=g.client.configInfo||{},g.client.configInfo.coldConfigData=
p,g.client.configInfo.coldHashData=n,g.client.configInfo.hotHashData=k);p=hl(C.location.href);!S("web_populate_internal_geo_killswitch")&&p.internalcountrycode&&(h.internalGeo=p.internalcountrycode);"MWEB"===h.clientName||"WEB"===h.clientName?(h.mainAppWebInfo={graftUrl:C.location.href},S("kevlar_woffle")&&Zl.h&&(p=Zl.h,h.mainAppWebInfo.pwaInstallabilityStatus=!p.h&&p.i?"PWA_INSTALLABILITY_STATUS_CAN_BE_INSTALLED":"PWA_INSTALLABILITY_STATUS_UNKNOWN"),h.mainAppWebInfo.webDisplayMode=$l(),h.mainAppWebInfo.isWebNativeShareAvailable=
navigator&&void 0!==navigator.share):"TVHTML5"===h.clientName&&(!S("web_lr_app_quality_killswitch")&&(p=R("LIVING_ROOM_APP_QUALITY"))&&(h.tvAppInfo=Object.assign(h.tvAppInfo||{},{appQuality:p})),p=R("LIVING_ROOM_CERTIFICATION_SCOPE"))&&(h.tvAppInfo=Object.assign(h.tvAppInfo||{},{certificationScope:p}));if(!S("web_populate_time_zone_itc_killswitch")){b:{if("undefined"!==typeof Intl)try{var r=(new Intl.DateTimeFormat).resolvedOptions().timeZone;break b}catch(fa){}r=void 0}r&&(h.timeZone=r)}(r=R("EXPERIMENTS_TOKEN",
""))?h.experimentsToken=r:delete h.experimentsToken;r=sl();Pu.h||(Pu.h=new Pu);h=Pu.h.h;p=[];n=0;for(var t in h)p[n++]=h[t];g.request=Object.assign({},g.request,{internalExperimentFlags:r,consistencyTokenJars:p});!S("web_prequest_context_killswitch")&&(t=R("INNERTUBE_CONTEXT_PREQUEST_CONTEXT"))&&(g.request.externalPrequestContext=t);r=hm();t=km(58);r=r.get("gsml","");g.user=Object.assign({},g.user);t&&(g.user.enableSafetyMode=t);r&&(g.user.lockedSafetyMode=!0);S("warm_op_csn_cleanup")?e&&(f=nt())&&
(g.clientScreenNonce=f):!f&&(f=nt())&&(g.clientScreenNonce=f);d&&(g.clickTracking={clickTrackingParams:d});if(d=E("yt.mdx.remote.remoteClient_"))g.remoteClient=d;Vu().setLocationOnInnerTubeContext(g);try{var x=kl(),z=x.bid;delete x.bid;g.adSignalsInfo={params:[],bid:z};var y=v(Object.entries(x));for(var J=y.next();!J.done;J=y.next()){var G=v(J.value),M=G.next().value,P=G.next().value;x=M;z=P;d=void 0;null==(d=g.adSignalsInfo.params)||d.push({key:x,value:""+z})}var ea;if(S("add_ifa_to_tvh5_requests")&&
"TVHTML5"===(null==(ea=g.client)?void 0:ea.clientName)){var aa=R("INNERTUBE_CONTEXT");aa.adSignalsInfo&&(g.adSignalsInfo.advertisingId=aa.adSignalsInfo.advertisingId,g.adSignalsInfo.limitAdTracking=aa.adSignalsInfo.limitAdTracking)}}catch(fa){Us(fa)}y=g}else Us(Error("Error: No InnerTubeContext shell provided in ytconfig.")),y={};y={context:y};if(J=this.i(a)){this.h(y,J,b);var U;b="/youtubei/v1/"+av(this.j());(J=null==(U=as(a.commandMetadata,Ck))?void 0:U.apiUrl)&&(b=J);U=b;(b=R("INNERTUBE_HOST_OVERRIDE"))&&
(U=String(b)+String(dc(U)));b={};S("web_api_key_killswitch")&&(b.key=R("INNERTUBE_API_KEY"));S("json_condensed_response")&&(b.prettyPrint="false");U=il(U,b||{},!1);a=Object.assign({},{command:a},void 0);a={input:U,ib:xt(U),Ma:y,config:a};a.config.Tb?a.config.Tb.identity=c:a.config.Tb={identity:c};return a}Us(new V("Error: Failed to create Request from Command.",a))};
ha.Object.defineProperties(bv.prototype,{l:{configurable:!0,enumerable:!0,get:function(){return!1}}});
function cv(){}
w(cv,bv);function dv(){}
w(dv,cv);dv.prototype.v=function(){return{input:"/getDatasyncIdsEndpoint",ib:xt("/getDatasyncIdsEndpoint","GET"),Ma:{}}};
dv.prototype.j=function(){return[]};
dv.prototype.i=function(){};
dv.prototype.h=function(){};var ev={},fv=(ev.GET_DATASYNC_IDS=Yu(dv),ev);function gv(a){var b;(b=E("ytcsi."+(a||"")+"data_"))||(b={tick:{},info:{}},D("ytcsi."+(a||"")+"data_",b));return b}
function hv(){var a=gv();a.info||(a.info={});return a.info}
function iv(a){a=gv(a);a.metadata||(a.metadata={});return a.metadata}
function jv(a){a=gv(a);a.tick||(a.tick={});return a.tick}
function kv(a){a=gv(a);if(a.gel){var b=a.gel;b.gelInfos||(b.gelInfos={});b.gelTicks||(b.gelTicks={})}else a.gel={gelTicks:{},gelInfos:{}};return a.gel}
function lv(a){a=kv(a);a.gelInfos||(a.gelInfos={});return a.gelInfos}
function mv(a){var b=gv(a).nonce;if(!b){if(S("enable_lr_96_bit_can_no_crypto")){b=bt();for(var c=[],d=0;d<b.length;d++)c.push("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_".charAt(b[d]&63));b=c.join("")}else b=ct();gv(a).nonce=b}return b}
;function nv(){var a=E("ytcsi.debug");a||(a=[],D("ytcsi.debug",a),D("ytcsi.reference",{}));return a}
function ov(a){a=a||"";var b=E("ytcsi.reference");b||(nv(),b=E("ytcsi.reference"));if(b[a])return b[a];var c=nv(),d={timerName:a,info:{},tick:{},span:{},jspbInfo:[]};c.push(d);return b[a]=d}
;var X={},pv=(X.auto_search="LATENCY_ACTION_AUTO_SEARCH",X.ad_to_ad="LATENCY_ACTION_AD_TO_AD",X.ad_to_video="LATENCY_ACTION_AD_TO_VIDEO",X["analytics.explore"]="LATENCY_ACTION_CREATOR_ANALYTICS_EXPLORE",X.app_startup="LATENCY_ACTION_APP_STARTUP",X["artist.analytics"]="LATENCY_ACTION_CREATOR_ARTIST_ANALYTICS",X["artist.events"]="LATENCY_ACTION_CREATOR_ARTIST_CONCERTS",X["artist.presskit"]="LATENCY_ACTION_CREATOR_ARTIST_PROFILE",X["asset.claimed_videos"]="LATENCY_ACTION_CREATOR_CMS_ASSET_CLAIMED_VIDEOS",
X["asset.composition"]="LATENCY_ACTION_CREATOR_CMS_ASSET_COMPOSITION",X["asset.composition_ownership"]="LATENCY_ACTION_CREATOR_CMS_ASSET_COMPOSITION_OWNERSHIP",X["asset.composition_policy"]="LATENCY_ACTION_CREATOR_CMS_ASSET_COMPOSITION_POLICY",X["asset.embeds"]="LATENCY_ACTION_CREATOR_CMS_ASSET_EMBEDS",X["asset.history"]="LATENCY_ACTION_CREATOR_CMS_ASSET_HISTORY",X["asset.issues"]="LATENCY_ACTION_CREATOR_CMS_ASSET_ISSUES",X["asset.licenses"]="LATENCY_ACTION_CREATOR_CMS_ASSET_LICENSES",X["asset.metadata"]=
"LATENCY_ACTION_CREATOR_CMS_ASSET_METADATA",X["asset.ownership"]="LATENCY_ACTION_CREATOR_CMS_ASSET_OWNERSHIP",X["asset.policy"]="LATENCY_ACTION_CREATOR_CMS_ASSET_POLICY",X["asset.references"]="LATENCY_ACTION_CREATOR_CMS_ASSET_REFERENCES",X["asset.shares"]="LATENCY_ACTION_CREATOR_CMS_ASSET_SHARES",X["asset.sound_recordings"]="LATENCY_ACTION_CREATOR_CMS_ASSET_SOUND_RECORDINGS",X["asset_group.assets"]="LATENCY_ACTION_CREATOR_CMS_ASSET_GROUP_ASSETS",X["asset_group.campaigns"]="LATENCY_ACTION_CREATOR_CMS_ASSET_GROUP_CAMPAIGNS",
X["asset_group.claimed_videos"]="LATENCY_ACTION_CREATOR_CMS_ASSET_GROUP_CLAIMED_VIDEOS",X["asset_group.metadata"]="LATENCY_ACTION_CREATOR_CMS_ASSET_GROUP_METADATA",X["song.analytics"]="LATENCY_ACTION_CREATOR_SONG_ANALYTICS",X.browse="LATENCY_ACTION_BROWSE",X.cast_splash="LATENCY_ACTION_CAST_SPLASH",X.channels="LATENCY_ACTION_CHANNELS",X.creator_channel_dashboard="LATENCY_ACTION_CREATOR_CHANNEL_DASHBOARD",X["channel.analytics"]="LATENCY_ACTION_CREATOR_CHANNEL_ANALYTICS",X["channel.comments"]="LATENCY_ACTION_CREATOR_CHANNEL_COMMENTS",
X["channel.content"]="LATENCY_ACTION_CREATOR_POST_LIST",X["channel.content.promotions"]="LATENCY_ACTION_CREATOR_PROMOTION_LIST",X["channel.copyright"]="LATENCY_ACTION_CREATOR_CHANNEL_COPYRIGHT",X["channel.editing"]="LATENCY_ACTION_CREATOR_CHANNEL_EDITING",X["channel.monetization"]="LATENCY_ACTION_CREATOR_CHANNEL_MONETIZATION",X["channel.music"]="LATENCY_ACTION_CREATOR_CHANNEL_MUSIC",X["channel.music_storefront"]="LATENCY_ACTION_CREATOR_CHANNEL_MUSIC_STOREFRONT",X["channel.playlists"]="LATENCY_ACTION_CREATOR_CHANNEL_PLAYLISTS",
X["channel.translations"]="LATENCY_ACTION_CREATOR_CHANNEL_TRANSLATIONS",X["channel.videos"]="LATENCY_ACTION_CREATOR_CHANNEL_VIDEOS",X["channel.live_streaming"]="LATENCY_ACTION_CREATOR_LIVE_STREAMING",X.chips="LATENCY_ACTION_CHIPS",X.commerce_transaction="LATENCY_ACTION_COMMERCE_TRANSACTION",X["dialog.copyright_strikes"]="LATENCY_ACTION_CREATOR_DIALOG_COPYRIGHT_STRIKES",X["dialog.video_copyright"]="LATENCY_ACTION_CREATOR_DIALOG_VIDEO_COPYRIGHT",X["dialog.uploads"]="LATENCY_ACTION_CREATOR_DIALOG_UPLOADS",
X.direct_playback="LATENCY_ACTION_DIRECT_PLAYBACK",X.embed="LATENCY_ACTION_EMBED",X.entity_key_serialization_perf="LATENCY_ACTION_ENTITY_KEY_SERIALIZATION_PERF",X.entity_key_deserialization_perf="LATENCY_ACTION_ENTITY_KEY_DESERIALIZATION_PERF",X.explore="LATENCY_ACTION_EXPLORE",X.favorites="LATENCY_ACTION_FAVORITES",X.home="LATENCY_ACTION_HOME",X.inboarding="LATENCY_ACTION_INBOARDING",X.library="LATENCY_ACTION_LIBRARY",X.live="LATENCY_ACTION_LIVE",X.live_pagination="LATENCY_ACTION_LIVE_PAGINATION",
X.mini_app="LATENCY_ACTION_MINI_APP_PLAY",X.onboarding="LATENCY_ACTION_ONBOARDING",X.owner="LATENCY_ACTION_CREATOR_CMS_DASHBOARD",X["owner.allowlist"]="LATENCY_ACTION_CREATOR_CMS_ALLOWLIST",X["owner.analytics"]="LATENCY_ACTION_CREATOR_CMS_ANALYTICS",X["owner.art_tracks"]="LATENCY_ACTION_CREATOR_CMS_ART_TRACKS",X["owner.assets"]="LATENCY_ACTION_CREATOR_CMS_ASSETS",X["owner.asset_groups"]="LATENCY_ACTION_CREATOR_CMS_ASSET_GROUPS",X["owner.bulk"]="LATENCY_ACTION_CREATOR_CMS_BULK_HISTORY",X["owner.campaigns"]=
"LATENCY_ACTION_CREATOR_CMS_CAMPAIGNS",X["owner.channel_invites"]="LATENCY_ACTION_CREATOR_CMS_CHANNEL_INVITES",X["owner.channels"]="LATENCY_ACTION_CREATOR_CMS_CHANNELS",X["owner.claimed_videos"]="LATENCY_ACTION_CREATOR_CMS_CLAIMED_VIDEOS",X["owner.claims"]="LATENCY_ACTION_CREATOR_CMS_MANUAL_CLAIMING",X["owner.claims.manual"]="LATENCY_ACTION_CREATOR_CMS_MANUAL_CLAIMING",X["owner.delivery"]="LATENCY_ACTION_CREATOR_CMS_CONTENT_DELIVERY",X["owner.delivery_templates"]="LATENCY_ACTION_CREATOR_CMS_DELIVERY_TEMPLATES",
X["owner.issues"]="LATENCY_ACTION_CREATOR_CMS_ISSUES",X["owner.licenses"]="LATENCY_ACTION_CREATOR_CMS_LICENSES",X["owner.pitch_music"]="LATENCY_ACTION_CREATOR_CMS_PITCH_MUSIC",X["owner.policies"]="LATENCY_ACTION_CREATOR_CMS_POLICIES",X["owner.releases"]="LATENCY_ACTION_CREATOR_CMS_RELEASES",X["owner.reports"]="LATENCY_ACTION_CREATOR_CMS_REPORTS",X["owner.videos"]="LATENCY_ACTION_CREATOR_CMS_VIDEOS",X.parent_profile_settings="LATENCY_ACTION_KIDS_PARENT_PROFILE_SETTINGS",X.parent_tools_collection="LATENCY_ACTION_PARENT_TOOLS_COLLECTION",
X.parent_tools_dashboard="LATENCY_ACTION_PARENT_TOOLS_DASHBOARD",X.player_att="LATENCY_ACTION_PLAYER_ATTESTATION",X["playlist.videos"]="LATENCY_ACTION_CREATOR_PLAYLIST_VIDEO_LIST",X["post.comments"]="LATENCY_ACTION_CREATOR_POST_COMMENTS",X["post.edit"]="LATENCY_ACTION_CREATOR_POST_EDIT",X.prebuffer="LATENCY_ACTION_PREBUFFER",X.prefetch="LATENCY_ACTION_PREFETCH",X.profile_settings="LATENCY_ACTION_KIDS_PROFILE_SETTINGS",X.profile_switcher="LATENCY_ACTION_LOGIN",X.reel_watch="LATENCY_ACTION_REEL_WATCH",
X.results="LATENCY_ACTION_RESULTS",X["promotion.edit"]="LATENCY_ACTION_CREATOR_PROMOTION_EDIT",X.red="LATENCY_ACTION_PREMIUM_PAGE_GET_BROWSE",X.premium="LATENCY_ACTION_PREMIUM_PAGE_GET_BROWSE",X.search_ui="LATENCY_ACTION_SEARCH_UI",X.search_suggest="LATENCY_ACTION_SUGGEST",X.search_zero_state="LATENCY_ACTION_SEARCH_ZERO_STATE",X.secret_code="LATENCY_ACTION_KIDS_SECRET_CODE",X.seek="LATENCY_ACTION_PLAYER_SEEK",X.settings="LATENCY_ACTION_SETTINGS",X.store="LATENCY_ACTION_STORE",X.tenx="LATENCY_ACTION_TENX",
X.video_to_ad="LATENCY_ACTION_VIDEO_TO_AD",X.watch="LATENCY_ACTION_WATCH",X.watch_it_again="LATENCY_ACTION_KIDS_WATCH_IT_AGAIN",X["watch,watch7"]="LATENCY_ACTION_WATCH",X["watch,watch7_html5"]="LATENCY_ACTION_WATCH",X["watch,watch7ad"]="LATENCY_ACTION_WATCH",X["watch,watch7ad_html5"]="LATENCY_ACTION_WATCH",X.wn_comments="LATENCY_ACTION_LOAD_COMMENTS",X.ww_rqs="LATENCY_ACTION_WHO_IS_WATCHING",X["video.analytics"]="LATENCY_ACTION_CREATOR_VIDEO_ANALYTICS",X["video.claims"]="LATENCY_ACTION_CREATOR_VIDEO_CLAIMS",
X["video.comments"]="LATENCY_ACTION_CREATOR_VIDEO_COMMENTS",X["video.copyright"]="LATENCY_ACTION_CREATOR_VIDEO_COPYRIGHT",X["video.edit"]="LATENCY_ACTION_CREATOR_VIDEO_EDIT",X["video.editor"]="LATENCY_ACTION_CREATOR_VIDEO_VIDEO_EDITOR",X["video.editor_async"]="LATENCY_ACTION_CREATOR_VIDEO_VIDEO_EDITOR_ASYNC",X["video.live_settings"]="LATENCY_ACTION_CREATOR_VIDEO_LIVE_SETTINGS",X["video.live_streaming"]="LATENCY_ACTION_CREATOR_VIDEO_LIVE_STREAMING",X["video.monetization"]="LATENCY_ACTION_CREATOR_VIDEO_MONETIZATION",
X["video.policy"]="LATENCY_ACTION_CREATOR_VIDEO_POLICY",X["video.rights_management"]="LATENCY_ACTION_CREATOR_VIDEO_RIGHTS_MANAGEMENT",X["video.translations"]="LATENCY_ACTION_CREATOR_VIDEO_TRANSLATIONS",X.voice_assistant="LATENCY_ACTION_VOICE_ASSISTANT",X.cast_load_by_entity_to_watch="LATENCY_ACTION_CAST_LOAD_BY_ENTITY_TO_WATCH",X.networkless_performance="LATENCY_ACTION_NETWORKLESS_PERFORMANCE",X.gel_compression="LATENCY_ACTION_GEL_COMPRESSION",X.gel_jspb_serialize="LATENCY_ACTION_GEL_JSPB_SERIALIZE",
X);function qv(a,b){gp.call(this,1,arguments);this.timer=b}
w(qv,gp);var rv=new hp("aft-recorded",qv);var sv=C.ytLoggingLatencyUsageStats_||{};D("ytLoggingLatencyUsageStats_",sv);function tv(){this.h=0}
function uv(){tv.h||(tv.h=new tv);return tv.h}
tv.prototype.tick=function(a,b,c,d){vv(this,"tick_"+a+"_"+b)||ln("latencyActionTicked",{tickName:a,clientActionNonce:b},{timestamp:c,cttAuthInfo:d})};
tv.prototype.info=function(a,b,c){var d=Object.keys(a).join("");vv(this,"info_"+d+"_"+b)||(a=Object.assign({},a),a.clientActionNonce=b,ln("latencyActionInfo",a,{cttAuthInfo:c}))};
tv.prototype.jspbInfo=function(){};
tv.prototype.span=function(a,b,c){var d=Object.keys(a).join("");vv(this,"span_"+d+"_"+b)||(a.clientActionNonce=b,ln("latencyActionSpan",a,{cttAuthInfo:c}))};
function vv(a,b){sv[b]=sv[b]||{count:0};var c=sv[b];c.count++;c.time=W();a.h||(a.h=um(function(){var d=W(),e;for(e in sv)sv[e]&&6E4<d-sv[e].time&&delete sv[e];a&&(a.h=0)},5E3));
return 5<c.count?(6===c.count&&1>1E5*Math.random()&&(c=new V("CSI data exceeded logging limit with key",b.split("_")),0<=b.indexOf("plev")||Vs(c)),!0):!1}
;var wv=window;function xv(){this.timing={};this.clearResourceTimings=function(){};
this.webkitClearResourceTimings=function(){};
this.mozClearResourceTimings=function(){};
this.msClearResourceTimings=function(){};
this.oClearResourceTimings=function(){}}
function yv(){var a;if(S("csi_use_performance_navigation_timing")||S("csi_use_performance_navigation_timing_tvhtml5")){var b,c,d,e=null==Y?void 0:null==(a=Y.getEntriesByType)?void 0:null==(b=a.call(Y,"navigation"))?void 0:null==(c=b[0])?void 0:null==(d=c.toJSON)?void 0:d.call(c);e?(e.requestStart=zv(e.requestStart),e.responseEnd=zv(e.responseEnd),e.redirectStart=zv(e.redirectStart),e.redirectEnd=zv(e.redirectEnd),e.domainLookupEnd=zv(e.domainLookupEnd),e.connectStart=zv(e.connectStart),e.connectEnd=
zv(e.connectEnd),e.responseStart=zv(e.responseStart),e.secureConnectionStart=zv(e.secureConnectionStart),e.domainLookupStart=zv(e.domainLookupStart),e.isPerformanceNavigationTiming=!0,a=e):a=Y.timing}else a=Y.timing;return a}
function zv(a){return Math.round(Av()+a)}
function Av(){return(S("csi_use_time_origin")||S("csi_use_time_origin_tvhtml5"))&&Y.timeOrigin?Math.floor(Y.timeOrigin):Y.timing.navigationStart}
var Y=wv.performance||wv.mozPerformance||wv.msPerformance||wv.webkitPerformance||new xv;var Bv=!1,Cv=!1,Dv={'script[name="scheduler/scheduler"]':"sj",'script[name="player/base"]':"pj",'link[rel="preload"][name="player/embed"]':"pej",'link[rel="stylesheet"][name="www-player"]':"pc",'link[rel="stylesheet"][name="player/www-player"]':"pc",'script[name="desktop_polymer/desktop_polymer"]':"dpj",'link[rel="import"][name="desktop_polymer"]':"dph",'script[name="mobile-c3"]':"mcj",'link[rel="stylesheet"][name="mobile-c3"]':"mcc",'script[name="player-plasma-ias-phone/base"]':"mcppj",'script[name="player-plasma-ias-tablet/base"]':"mcptj",
'link[rel="stylesheet"][name="mobile-polymer-player-ias"]':"mcpc",'link[rel="stylesheet"][name="mobile-polymer-player-svg-ias"]':"mcpsc",'script[name="mobile_blazer_core_mod"]':"mbcj",'link[rel="stylesheet"][name="mobile_blazer_css"]':"mbc",'script[name="mobile_blazer_logged_in_users_mod"]':"mbliuj",'script[name="mobile_blazer_logged_out_users_mod"]':"mblouj",'script[name="mobile_blazer_noncore_mod"]':"mbnj","#player_css":"mbpc",'script[name="mobile_blazer_desktopplayer_mod"]':"mbpj",'link[rel="stylesheet"][name="mobile_blazer_tablet_css"]':"mbtc",
'script[name="mobile_blazer_watch_mod"]':"mbwj"};Xa(Y.clearResourceTimings||Y.webkitClearResourceTimings||Y.mozClearResourceTimings||Y.msClearResourceTimings||Y.oClearResourceTimings||db,Y);function Ev(a,b){if(!S("web_csi_action_sampling_enabled")||!gv(b).actionDisabled){var c=ov(b||"");ku(c.info,a);a.loadType&&(c=a.loadType,iv(b).loadType=c);ku(lv(b),a);c=mv(b);b=gv(b).cttAuthInfo;uv().info(a,c,b)}}
function Fv(){var a,b,c,d;return(null!=(d=null==Er().resolve(new yr(Wo))?void 0:null==(a=Xo())?void 0:null==(b=a.loggingHotConfig)?void 0:null==(c=b.csiConfig)?void 0:c.debugTicks)?d:[]).map(function(e){return Object.values(e)[0]})}
function Z(a,b,c){if(!S("web_csi_action_sampling_enabled")||!gv(c).actionDisabled){var d=mv(c),e;if(e=S("web_csi_debug_sample_enabled")&&d){(null==Er().resolve(new yr(Wo))?0:Xo())&&!Cv&&(Cv=!0,Z("gcfl",W(),c));var f,g,h;e=(null==Er().resolve(new yr(Wo))?void 0:null==(f=Xo())?void 0:null==(g=f.loggingHotConfig)?void 0:null==(h=g.csiConfig)?void 0:h.debugSampleWeight)||0;if(f=0!==e)b:{f=Fv();if(0<f.length)for(g=0;g<f.length;g++)if(a===f[g]){f=!0;break b}f=!1}if(f){for(g=f=0;g<d.length;g++)f=31*f+d.charCodeAt(g),
g<d.length-1&&(f%=Math.pow(2,47));e=0!==f%1E5%e;gv(c).debugTicksExcludedLogged||(f={},f.debugTicksExcluded=e,Ev(f,c));gv(c).debugTicksExcludedLogged=!0}else e=!1}if(!e){b||"_"===a[0]||(e=a,Y.mark&&(e.startsWith("mark_")||(e="mark_"+e),c&&(e+=" ("+c+")"),Y.mark(e)));e=ov(c||"");e.tick[a]=b||W();if(e.callback&&e.callback[a])for(e=v(e.callback[a]),f=e.next();!f.done;f=e.next())f=f.value,f();e=kv(c);e.gelTicks&&(e.gelTicks[a]=!0);f=jv(c);e=b||W();S("log_repeated_ytcsi_ticks")?a in f||(f[a]=e):f[a]=e;
f=gv(c).cttAuthInfo;"_start"===a?(a=uv(),vv(a,"baseline_"+d)||ln("latencyActionBaselined",{clientActionNonce:d},{timestamp:b,cttAuthInfo:f})):uv().tick(a,d,b,f);Gv(c);return e}}}
function Hv(){var a=document;if("visibilityState"in a)a=a.visibilityState;else{var b=Vq+"VisibilityState";a=b in a?a[b]:void 0}switch(a){case "hidden":return 0;case "visible":return 1;case "prerender":return 2;case "unloaded":return 3;default:return-1}}
function Iv(){function a(f,g,h){g=g.match("_rid")?g.split("_rid")[0]:g;"number"===typeof h&&(h=JSON.stringify(h));f.requestIds?f.requestIds.push({endpoint:g,id:h}):f.requestIds=[{endpoint:g,id:h}]}
for(var b={},c=v(Object.entries(R("TIMING_INFO",{}))),d=c.next();!d.done;d=c.next()){var e=v(d.value);d=e.next().value;e=e.next().value;switch(d){case "GetBrowse_rid":a(b,d,e);break;case "GetGuide_rid":a(b,d,e);break;case "GetHome_rid":a(b,d,e);break;case "GetPlayer_rid":a(b,d,e);break;case "GetSearch_rid":a(b,d,e);break;case "GetSettings_rid":a(b,d,e);break;case "GetTrending_rid":a(b,d,e);break;case "GetWatchNext_rid":a(b,d,e);break;case "yt_red":b.isRedSubscriber=!!e;break;case "yt_ad":b.isMonetized=
!!e}}return b}
function Jv(a,b){a=document.querySelector(a);if(!a)return!1;var c="",d=a.nodeName;"SCRIPT"===d?(c=a.src,c||(c=a.getAttribute("data-timing-href"))&&(c=window.location.protocol+c)):"LINK"===d&&(c=a.href);fi(window)&&a.setAttribute("nonce",fi(window));return c?(a=Y.getEntriesByName(c))&&a[0]&&(a=a[0],c=Av(),Z("rsf_"+b,c+Math.round(a.fetchStart)),Z("rse_"+b,c+Math.round(a.responseEnd)),void 0!==a.transferSize&&0===a.transferSize)?!0:!1:!1}
function Kv(){var a=window.location.protocol,b=Y.getEntriesByType("resource");b=hb(b,function(c){return 0===c.name.indexOf(a+"//fonts.gstatic.com/s/")});
(b=jb(b,function(c,d){return d.duration>c.duration?d:c},{duration:0}))&&0<b.startTime&&0<b.responseEnd&&(Z("wffs",zv(b.startTime)),Z("wffe",zv(b.responseEnd)))}
function Lv(a){var b=Mv("aft",a);if(b)return b;b=R((a||"")+"TIMING_AFT_KEYS",["ol"]);for(var c=b.length,d=0;d<c;d++){var e=Mv(b[d],a);if(e)return e}return NaN}
function Mv(a,b){if(a=jv(b)[a])return"number"===typeof a?a:a[a.length-1]}
function Gv(a){var b=Mv("_start",a),c=Lv(a);b&&c&&!Bv&&(mp(rv,new qv(Math.round(c-b),a)),Bv=!0)}
function Nv(){if(Y.getEntriesByType){var a=Y.getEntriesByType("paint");if(a=kb(a,function(b){return"first-paint"===b.name}))return zv(a.startTime)}a=Y.timing;
return a.Ae?Math.max(0,a.Ae):0}
;function Ov(a,b){Yk(function(){ov("").info.actionType=a;b&&Uk("TIMING_AFT_KEYS",b);Uk("TIMING_ACTION",a);var c=Iv();0<Object.keys(c).length&&Ev(c);c={isNavigation:!0,actionType:pv[R("TIMING_ACTION")]||"LATENCY_ACTION_UNKNOWN"};var d=R("PREVIOUS_ACTION");d&&(c.previousAction=pv[d]||"LATENCY_ACTION_UNKNOWN");if(d=R("CLIENT_PROTOCOL"))c.httpProtocol=d;if(d=R("CLIENT_TRANSPORT"))c.transportProtocol=d;(d=nt())&&"UNDEFINED_CSN"!==d&&(c.clientScreenNonce=d);d=Hv();if(1===d||-1===d)c.isVisible=!0;iv();hv();
c.loadType="cold";d=hv();var e=yv(),f=Av(),g=R("CSI_START_TIMESTAMP_MILLIS",0);0<g&&!S("embeds_web_enable_csi_start_override_killswitch")&&(f=g);f&&(Z("srt",e.responseStart),1!==d.prerender&&Z("_start",f,void 0));d=Nv();0<d&&Z("fpt",d);d=yv();d.isPerformanceNavigationTiming&&Ev({performanceNavigationTiming:!0},void 0);Z("nreqs",d.requestStart,void 0);Z("nress",d.responseStart,void 0);Z("nrese",d.responseEnd,void 0);0<d.redirectEnd-d.redirectStart&&(Z("nrs",d.redirectStart,void 0),Z("nre",d.redirectEnd,
void 0));0<d.domainLookupEnd-d.domainLookupStart&&(Z("ndnss",d.domainLookupStart,void 0),Z("ndnse",d.domainLookupEnd,void 0));0<d.connectEnd-d.connectStart&&(Z("ntcps",d.connectStart,void 0),Z("ntcpe",d.connectEnd,void 0));d.secureConnectionStart>=Av()&&0<d.connectEnd-d.secureConnectionStart&&(Z("nstcps",d.secureConnectionStart,void 0),Z("ntcpe",d.connectEnd,void 0));Y&&"getEntriesByType"in Y&&Kv();d=[];if(document.querySelector&&Y&&Y.getEntriesByName)for(var h in Dv)Dv.hasOwnProperty(h)&&(e=Dv[h],
Jv(h,e)&&d.push(e));if(0<d.length)for(c.resourceInfo=[],h=v(d),d=h.next();!d.done;d=h.next())c.resourceInfo.push({resourceCache:d.value});Ev(c);c=kv();c.preLoggedGelInfos||(c.preLoggedGelInfos=[]);h=c.preLoggedGelInfos;c=lv();d=void 0;for(e=0;e<h.length;e++)if(f=h[e],f.loadType){d=f.loadType;break}if("cold"===iv().loadType&&("cold"===c.loadType||"cold"===d)){d=jv();e=kv();e=e.gelTicks?e.gelTicks:e.gelTicks={};for(var k in d)if(!(k in e))if("number"===typeof d[k])Z(k,Mv(k));else if(S("log_repeated_ytcsi_ticks"))for(f=
v(d[k]),g=f.next();!g.done;g=f.next())g=g.value,Z(k.slice(1),g);k={};d=!1;h=v(h);for(e=h.next();!e.done;e=h.next())d=e.value,ku(c,d),ku(k,d),d=!0;d&&Ev(k)}D("ytglobal.timingready_",!0);k=R("TIMING_ACTION");E("ytglobal.timingready_")&&k&&Pv()&&Lv()&&Gv()})()}
function Qv(a,b,c){Yk(Ev)(a,b,void 0===c?!1:c)}
function Rv(a,b,c){return Yk(Z)(a,b,c)}
function Pv(){return Yk(function(){return"_start"in jv()})()}
function Sv(){Yk(function(){var a=mv();requestAnimationFrame(function(){setTimeout(function(){a===mv()&&Rv("ol",void 0,void 0)},0)})})()}
var Tv=window;Tv.ytcsi&&(Tv.ytcsi.infoGel=Qv,Tv.ytcsi.tick=Rv);var Uv="tokens consistency mss client_location entities adblock_detection response_received_commands store PLAYER_PRELOAD".split(" "),Vv=["type.googleapis.com/youtube.api.pfiinnertube.YoutubeApiInnertube.BrowseResponse","type.googleapis.com/youtube.api.pfiinnertube.YoutubeApiInnertube.PlayerResponse"];function Wv(a,b,c,d){this.v=a;this.aa=b;this.l=c;this.j=d;this.i=void 0;this.h=new Map;a.Ob||(a.Ob={});a.Ob=Object.assign({},fv,a.Ob)}
function Xv(a,b,c,d){if(void 0!==Wv.h){if(d=Wv.h,a=[a!==d.v,b!==d.aa,c!==d.l,!1,!1,!1,void 0!==d.i],a.some(function(e){return e}))throw new V("InnerTubeTransportService is already initialized",a);
}else Wv.h=new Wv(a,b,c,d)}
function Yv(a){var b={signalServiceEndpoint:{signal:"GET_DATASYNC_IDS"}};var c=void 0===c?Yl:c;var d=Wu(b,a.v);if(!d)return Pd(new V("Error: No request builder found for command.",b));var e=d.v(b,void 0,c);return e?(Ku(e.input),new Kd(function(f){var g,h,k;return A(function(l){if(1==l.h){h="cors"===(null==(g=e.ib)?void 0:g.mode)?"cors":void 0;if(a.l.df){var n=e.config,p;n=null==n?void 0:null==(p=n.Tb)?void 0:p.sessionIndex;p=Xl(0,{sessionIndex:n});k=Object.assign({},Xu(h),p);return l.B(2)}return l.yield(Zv(e.config,
h),3)}2!=l.h&&(k=l.i);f($v(a,e,k));l.h=0})})):Pd(new V("Error: Failed to build request for command.",b))}
function aw(a,b,c){var d;if(b&&!(null==b?0:null==(d=b.sequenceMetaData)?0:d.skipProcessing)&&a.j){d=v(Uv);for(var e=d.next();!e.done;e=d.next())e=e.value,a.j[e]&&a.j[e].handleResponse(b,c)}}
function $v(a,b,c){var d,e,f,g,h,k,l,n,p,r,t,x,z,y,J,G,M,P,ea,aa,U,fa,la,ma,Da,Rg,qr,rr,sr;return A(function(ia){switch(ia.h){case 1:ia.B(2);break;case 3:if((d=ia.i)&&!d.isExpired())return ia.return(Promise.resolve(d.h()));case 2:if(!(null==(e=b)?0:null==(f=e.Ma)?0:f.context)){ia.B(4);break}g=b.Ma.context;ia.B(5);break;case 5:h=v([]),k=h.next();case 7:if(k.done){ia.B(4);break}l=k.value;return ia.yield(l.ig(g),8);case 8:k=h.next();ia.B(7);break;case 4:if(null==(n=a.i)||!n.mg(b.input,b.Ma)){ia.B(11);
break}return ia.yield(a.i.dg(b.input,b.Ma),12);case 12:return p=ia.i,S("kevlar_process_local_innertube_responses_killswitch")||aw(a,p,b),ia.return(p);case 11:return(x=null==(t=b.config)?void 0:t.kg)&&a.h.has(x)?r=a.h.get(x):(z=JSON.stringify(b.Ma),G=null!=(J=null==(y=b.ib)?void 0:y.headers)?J:{},b.ib=Object.assign({},b.ib,{headers:Object.assign({},G,c)}),M=Object.assign({},b.ib),"POST"===b.ib.method&&(M=Object.assign({},M,{body:z})),(null==(P=b.config)?0:P.Ke)&&Rv(b.config.Ke),ea=function(){return a.aa.fetch(b.input,
M,b.config)},r=ea(),x&&a.h.set(x,r)),ia.yield(r,13);
case 13:if((aa=ia.i)&&"error"in aa&&(null==(U=aa)?0:null==(fa=U.error)?0:fa.details))for(la=aa.error.details,ma=v(la),Da=ma.next();!Da.done;Da=ma.next())Rg=Da.value,(qr=Rg["@type"])&&-1<Vv.indexOf(qr)&&(delete Rg["@type"],aa=Rg);x&&a.h.has(x)&&a.h.delete(x);(null==(rr=b.config)?0:rr.Le)&&Rv(b.config.Le);if(aa||null==(sr=a.i)||!sr.Vf(b.input,b.Ma)){ia.B(14);break}return ia.yield(a.i.cg(b.input,b.Ma),15);case 15:aa=ia.i;case 14:return aw(a,aa,b),ia.return(aa||void 0)}})}
function Zv(a,b){var c,d,e,f;return A(function(g){if(1==g.h){e=null==(c=a)?void 0:null==(d=c.Tb)?void 0:d.sessionIndex;var h=g.yield;var k=Xl(0,{sessionIndex:e});if(!(k instanceof Kd)){var l=new Kd(db);Ld(l,2,k);k=l}return h.call(g,k,2)}f=g.i;return g.return(Promise.resolve(Object.assign({},Xu(b),f)))})}
;var bw=new xr("INNERTUBE_TRANSPORT_TOKEN");function cw(){}
w(cw,cv);cw.prototype.j=function(){return Tt};
cw.prototype.i=function(a){return as(a,Lk)||void 0};
cw.prototype.h=function(a,b,c){c=void 0===c?{}:c;b.channelIds&&(a.channelIds=b.channelIds);b.siloName&&(a.siloName=b.siloName);b.params&&(a.params=b.params);c.botguardResponse&&(a.botguardResponse=c.botguardResponse);c.feature&&(a.clientFeature=c.feature)};
ha.Object.defineProperties(cw.prototype,{l:{configurable:!0,enumerable:!0,get:function(){return!0}}});function dw(){}
w(dw,cv);dw.prototype.j=function(){return Ut};
dw.prototype.i=function(a){return as(a,Kk)||void 0};
dw.prototype.h=function(a,b){b.channelIds&&(a.channelIds=b.channelIds);b.siloName&&(a.siloName=b.siloName);b.params&&(a.params=b.params)};
ha.Object.defineProperties(dw.prototype,{l:{configurable:!0,enumerable:!0,get:function(){return!0}}});function ew(){}
w(ew,cv);ew.prototype.j=function(){return Qt};
ew.prototype.i=function(a){return as(a,Fk)||void 0};
ew.prototype.h=function(a,b,c){a.feedbackTokens=[];b.feedbackToken&&a.feedbackTokens.push(b.feedbackToken);if(b=b.cpn||c.cpn)a.feedbackContext={cpn:b};a.isFeedbackTokenUnencrypted=!!c.is_feedback_token_unencrypted;a.shouldMerge=!1;c.extra_feedback_tokens&&(a.shouldMerge=!0,a.feedbackTokens=a.feedbackTokens.concat(c.extra_feedback_tokens))};
ha.Object.defineProperties(ew.prototype,{l:{configurable:!0,enumerable:!0,get:function(){return!0}}});function fw(){}
w(fw,cv);fw.prototype.j=function(){return Rt};
fw.prototype.i=function(a){return as(a,Jk)||void 0};
fw.prototype.h=function(a,b){b.params&&(a.params=b.params);b.secondaryParams&&(a.secondaryParams=b.secondaryParams)};function gw(){}
w(gw,cv);gw.prototype.j=function(){return St};
gw.prototype.i=function(a){return as(a,Ik)||void 0};
gw.prototype.h=function(a,b){b.actions&&(a.actions=b.actions);b.params&&(a.params=b.params);b.playlistId&&(a.playlistId=b.playlistId)};function hw(){}
w(hw,cv);hw.prototype.j=function(){return Pt};
hw.prototype.i=function(a){return as(a,Hk)};
hw.prototype.h=function(a,b,c){c=void 0===c?{}:c;b.serializedShareEntity&&(a.serializedSharedEntity=b.serializedShareEntity);c.includeListId&&(a.includeListId=!0)};function iw(a,b){var c=B.apply(2,arguments);a=void 0===a?0:a;V.call(this,b,c);this.errorType=a;Object.setPrototypeOf(this,this.constructor.prototype)}
w(iw,V);var jw=new xr("NETWORK_SLI_TOKEN");function kw(a){this.h=a}
kw.prototype.fetch=function(a,b,c){var d=this,e;return A(function(f){e=lw(d,a,b);return f.return(fetch(e).then(function(g){return d.handleResponse(g,c)}).catch(function(g){Vs(g);
if((null==c?0:c.be)&&g instanceof iw&&1===g.errorType)return Promise.reject(g)}))})};
function lw(a,b,c){if(a.h){var d=ac(bc(5,mc(b,"key")))||"/UNKNOWN_PATH";a.h.start(d)}a=c;S("wug_networking_gzip_request")&&(a=Op(c));return new window.Request(b,a)}
kw.prototype.handleResponse=function(a,b){var c=a.text().then(function(d){if((null==b?0:b.ue)&&a.ok)return eg(b.ue,d);d=d.replace(")]}'","");if((null==b?0:b.be)&&d)try{var e=JSON.parse(d)}catch(g){throw new iw(1,"JSON parsing failed after fetch");}var f;return null!=(f=e)?f:JSON.parse(d)});
a.redirected||a.ok?this.h&&this.h.success():(this.h&&this.h.Yf(),c=c.then(function(d){Vs(new V("Error: API fetch failed",a.status,a.url,d));return Object.assign({},d,{errorMetadata:{status:a.status}})}));
return c};
kw[wr]=[new yr(jw)];var mw=new xr("NETWORK_MANAGER_TOKEN");var nw;function ow(){var a,b,c;return A(function(d){if(1==d.h)return a=Er().resolve(bw),a?d.yield(Yv(a),2):(Vs(Error("InnertubeTransportService unavailable in fetchDatasyncIds")),d.return(void 0));if(b=d.i){if(b.errorMetadata)return Vs(Error("Datasync IDs fetch responded with "+b.errorMetadata.status+": "+b.error)),d.return(void 0);c=b.Wf;return d.return(c)}Vs(Error("Network request to get Datasync IDs failed."));return d.return(void 0)})}
;var pw=C.caches,qw;function rw(a){var b=a.indexOf(":");return-1===b?{sd:a}:{sd:a.substring(0,b),datasyncId:a.substring(b+1)}}
function sw(){return A(function(a){if(void 0!==qw)return a.return(qw);qw=new Promise(function(b){var c;return A(function(d){switch(d.h){case 1:return Ba(d,2),d.yield(pw.open("test-only"),4);case 4:return d.yield(pw.delete("test-only"),5);case 5:d.h=3;d.l=0;break;case 2:if(c=Ca(d),c instanceof Error&&"SecurityError"===c.name)return b(!1),d.return();case 3:b("caches"in window),d.h=0}})});
return a.return(qw)})}
function tw(a){var b,c,d,e,f,g,h;A(function(k){if(1==k.h)return k.yield(sw(),2);if(3!=k.h){if(!k.i)return k.return(!1);b=[];return k.yield(pw.keys(),3)}c=k.i;d=v(c);for(e=d.next();!e.done;e=d.next())f=e.value,g=rw(f),h=g.datasyncId,!h||a.includes(h)||b.push(pw.delete(f));return k.return(Promise.all(b).then(function(l){return l.some(function(n){return n})}))})}
function uw(){var a,b,c,d,e,f,g;return A(function(h){if(1==h.h)return h.yield(sw(),2);if(3!=h.h){if(!h.i)return h.return(!1);a=sm("cache contains other");return h.yield(pw.keys(),3)}b=h.i;c=v(b);for(d=c.next();!d.done;d=c.next())if(e=d.value,f=rw(e),(g=f.datasyncId)&&g!==a)return h.return(!0);return h.return(!1)})}
;function vw(){ow().then(function(a){a&&(Bo(a),tw(a),Hu(a))})}
function ww(){var a=new Gq;vi.pa(function(){var b,c,d,e;return A(function(f){switch(f.h){case 1:if(S("ytidb_clear_optimizations_killswitch")){f.B(2);break}b=sm("clear");if(b.startsWith("V")&&b.endsWith("||")){var g=[b];Bo(g);tw(g);Hu(g);return f.return()}c=Iu();return f.yield(uw(),3);case 3:return d=f.i,f.yield(Co(),4);case 4:if(e=f.i,!c&&!d&&!e)return f.return();case 2:a.wa()?vw():a.h.add("publicytnetworkstatus-online",vw,!0,void 0,void 0),f.h=0}})})}
;function xw(){this.state=1;this.h=null}
m=xw.prototype;m.initialize=function(a,b,c){if(a.program){var d,e=null!=(d=a.interpreterUrl)?d:null;if(a.interpreterSafeScript){var f=a.interpreterSafeScript;f?((f=f.privateDoNotAccessOrElseSafeScriptWrappedValue)?(f=(d=zb())?d.createScript(f):f,d=new Xb,d.ud=f,f=d):f=null,d=f):d=null}else d=null!=(f=a.interpreterScript)?f:null;a.interpreterSafeUrl&&(e=vk(a.interpreterSafeUrl).toString());yw(this,d,e,a.program,b,c)}else Vs(Error("Cannot initialize botguard without program"))};
function yw(a,b,c,d,e,f){var g=void 0===g?"trayride":g;c?(a.state=2,Zt(c,function(){window[g]?zw(a,d,g,e):(a.state=3,du(c),Vs(new V("Unable to load Botguard","from "+c)))},f)):b?(f=wd("SCRIPT"),b instanceof Xb?hi(f,b):f.textContent=b,f.nonce=fi(window),document.head.appendChild(f),document.head.removeChild(f),window[g]?zw(a,d,g,e):(a.state=4,Vs(new V("Unable to load Botguard from JS")))):Vs(new V("Unable to load VM; no url or JS provided"))}
m.isLoading=function(){return 2===this.state};
function zw(a,b,c,d){a.state=5;try{var e=Lh({program:b,ke:c,xd:S("att_web_record_metrics")});e.Ze.then(function(){a.state=6;d&&d(b)});
a.Qc(e)}catch(f){a.state=7,f instanceof Error&&Vs(f)}}
m.invoke=function(a){a=void 0===a?{}:a;return this.Tc()?this.Kd({dd:a}):null};
m.dispose=function(){this.Qc(null);this.state=8};
m.Tc=function(){return!!this.h};
m.Kd=function(a){return this.h.Ed(a)};
m.Qc=function(a){rc(this.h);this.h=a};var Aw=[],Bw=!1;function Cw(){if(!S("disable_biscotti_fetch_for_ad_blocker_detection")&&!S("disable_biscotti_fetch_entirely_for_all_web_clients")&&zt()){var a=R("PLAYER_VARS",{});if("1"!=sb(a)&&!At(a)){var b=function(){Bw=!0;"google_ad_status"in window?Uk("DCLKSTAT",1):Uk("DCLKSTAT",2)};
try{Zt("//static.doubleclick.net/instream/ad_status.js",b)}catch(c){}Aw.push(vi.pa(function(){if(!(Bw||"google_ad_status"in window)){try{eu("//static.doubleclick.net/instream/ad_status.js",b)}catch(c){}Bw=!0;Uk("DCLKSTAT",3)}},5E3))}}}
function Dw(){var a=Number(R("DCLKSTAT",0));return isNaN(a)?0:a}
;function Ew(){var a=E("yt.abuse.playerAttLoader");return a&&["bgvma","bgvmb","bgvmc"].every(function(b){return b in a})?a:null}
;function Fw(){xw.apply(this,arguments)}
w(Fw,xw);Fw.prototype.Qc=function(a){var b;null==(b=Ew())||b.bgvma();a?(b={bgvma:a.dispose.bind(a),bgvmb:a.snapshot.bind(a),bgvmc:a.Ed.bind(a)},D("yt.abuse.playerAttLoader",b),D("yt.abuse.playerAttLoaderRun",function(c){return a.snapshot(c)})):(D("yt.abuse.playerAttLoader",null),D("yt.abuse.playerAttLoaderRun",null))};
Fw.prototype.Tc=function(){return!!Ew()};
Fw.prototype.Kd=function(a){return Ew().bgvmc(a)};function Gw(a){Nr.call(this,void 0===a?"document_active":a);var b=this;this.l=10;this.h=new Map;this.transitions=[{from:"document_active",to:"document_disposed_preventable",action:this.D},{from:"document_active",to:"document_disposed",action:this.v},{from:"document_disposed_preventable",to:"document_disposed",action:this.v},{from:"document_disposed_preventable",to:"flush_logs",action:this.m},{from:"document_disposed_preventable",to:"document_active",action:this.i},{from:"document_disposed",to:"flush_logs",
action:this.m},{from:"document_disposed",to:"document_active",action:this.i},{from:"document_disposed",to:"document_disposed",action:function(){}},
{from:"flush_logs",to:"document_active",action:this.i}];window.addEventListener("pagehide",function(c){b.transition("document_disposed",{event:c})});
window.addEventListener("beforeunload",function(c){b.transition("document_disposed_preventable",{event:c})})}
w(Gw,Nr);Gw.prototype.D=function(a,b){if(!this.h.get("document_disposed_preventable")){a(null==b?void 0:b.event);var c,d;if((null==b?0:null==(c=b.event)?0:c.defaultPrevented)||(null==b?0:null==(d=b.event)?0:d.returnValue)){b.event.returnValue||(b.event.returnValue=!0);b.event.defaultPrevented||b.event.preventDefault();this.h=new Map;this.transition("document_active");return}}this.h.set("document_disposed_preventable",!0);this.h.get("document_disposed")?this.transition("flush_logs"):this.transition("document_disposed")};
Gw.prototype.v=function(a,b){this.h.get("document_disposed")?this.transition("document_active"):(a(null==b?void 0:b.event),this.h.set("document_disposed",!0),this.transition("flush_logs"))};
Gw.prototype.m=function(a,b){a(null==b?void 0:b.event);this.transition("document_active")};
Gw.prototype.i=function(){this.h=new Map};function Hw(a){Nr.call(this,void 0===a?"document_visibility_unknown":a);var b=this;this.transitions=[{from:"document_visibility_unknown",to:"document_visible",action:this.i},{from:"document_visibility_unknown",to:"document_hidden",action:this.h},{from:"document_visibility_unknown",to:"document_foregrounded",action:this.m},{from:"document_visibility_unknown",to:"document_backgrounded",action:this.v},{from:"document_visible",to:"document_hidden",action:this.h},{from:"document_visible",to:"document_foregrounded",
action:this.m},{from:"document_visible",to:"document_visible",action:this.i},{from:"document_foregrounded",to:"document_visible",action:this.i},{from:"document_foregrounded",to:"document_hidden",action:this.h},{from:"document_foregrounded",to:"document_foregrounded",action:this.m},{from:"document_hidden",to:"document_visible",action:this.i},{from:"document_hidden",to:"document_backgrounded",action:this.v},{from:"document_hidden",to:"document_hidden",action:this.h},{from:"document_backgrounded",to:"document_hidden",
action:this.h},{from:"document_backgrounded",to:"document_backgrounded",action:this.v},{from:"document_backgrounded",to:"document_visible",action:this.i}];document.addEventListener("visibilitychange",function(c){"visible"===document.visibilityState?b.transition("document_visible",{event:c}):b.transition("document_hidden",{event:c})});
S("visibility_lifecycles_dynamic_backgrounding")&&(window.addEventListener("blur",function(c){b.transition("document_backgrounded",{event:c})}),window.addEventListener("focus",function(c){b.transition("document_foregrounded",{event:c})}))}
w(Hw,Nr);Hw.prototype.i=function(a,b){a(null==b?void 0:b.event);S("visibility_lifecycles_dynamic_backgrounding")&&this.transition("document_foregrounded")};
Hw.prototype.h=function(a,b){a(null==b?void 0:b.event);S("visibility_lifecycles_dynamic_backgrounding")&&this.transition("document_backgrounded")};
Hw.prototype.v=function(a,b){a(null==b?void 0:b.event)};
Hw.prototype.m=function(a,b){a(null==b?void 0:b.event)};function Iw(){this.l=new Gw;this.v=new Hw}
Iw.prototype.install=function(){var a=B.apply(0,arguments),b=this;a.forEach(function(c){b.l.install(c)});
a.forEach(function(c){b.v.install(c)})};function Jw(){this.l=[];this.i=new Map;this.h=new Map;this.j=new Set}
Jw.prototype.clickCommand=function(a,b,c){var d=a.clickTrackingParams;c=void 0===c?0:c;if(d)if(c=nt(void 0===c?0:c)){a=this.client;d=new ft({trackingParams:d});var e=void 0;if(S("no_client_ve_attach_unless_shown")){var f=Cu(d,c);yu.set(f,!0);Du(d,c)}e=e||"INTERACTION_LOGGING_GESTURE_TYPE_GENERIC_CLICK";f=Bu({cttAuthInfo:pt(c)||void 0},c);d={csn:c,ve:d.getAsJson(),gestureType:e};b&&(d.clientData=b);"UNDEFINED_CSN"===c?Eu("visualElementGestured",f,d):a?Ns("visualElementGestured",d,a,f):ln("visualElementGestured",
d,f);b=!0}else b=!1;else b=!1;return b};
Jw.prototype.stateChanged=function(a,b,c){this.visualElementStateChanged(new ft({trackingParams:a}),b,void 0===c?0:c)};
Jw.prototype.visualElementStateChanged=function(a,b,c){c=void 0===c?0:c;if(0===c&&this.j.has(c))this.l.push([a,b]);else{var d=c;d=void 0===d?0:d;c=nt(d);a||(a=(a=kt(void 0===d?0:d))?new ft({veType:a,youtubeData:void 0,jspbYoutubeData:void 0}):null);var e=a;c&&e&&(a=this.client,d=Bu({cttAuthInfo:pt(c)||void 0},c),b={csn:c,ve:e.getAsJson(),clientData:b},"UNDEFINED_CSN"===c?Eu("visualElementStateChanged",d,b):a?Ns("visualElementStateChanged",b,a,d):ln("visualElementStateChanged",b,d))}};
function Kw(a,b){if(void 0===b)for(var c=mt(),d=0;d<c.length;d++)void 0!==c[d]&&Kw(a,c[d]);else a.i.forEach(function(e,f){(f=a.h.get(f))&&Au(a.client,b,f,e)}),a.i.clear(),a.h.clear()}
;function Lw(){Iw.call(this);var a={};this.install((a.document_disposed={callback:this.h},a));S("combine_ve_grafts")&&(a={},this.install((a.document_disposed={callback:this.i},a)));a={};this.install((a.flush_logs={callback:this.j},a))}
w(Lw,Iw);Lw.prototype.j=function(){ln("finalPayload",{csn:nt()})};
Lw.prototype.h=function(){Zs($s)};
Lw.prototype.i=function(){var a=Kw;Jw.h||(Jw.h=new Jw);a(Jw.h)};function Mw(){}
function Nw(){var a=E("ytglobal.storage_");a||(a=new Mw,D("ytglobal.storage_",a));return a}
Mw.prototype.estimate=function(){var a,b,c;return A(function(d){a=navigator;return(null==(b=a.storage)?0:b.estimate)?d.return(a.storage.estimate()):(null==(c=a.webkitTemporaryStorage)?0:c.queryUsageAndQuota)?d.return(Ow()):d.return()})};
function Ow(){var a=navigator;return new Promise(function(b,c){var d;null!=(d=a.webkitTemporaryStorage)&&d.queryUsageAndQuota?a.webkitTemporaryStorage.queryUsageAndQuota(function(e,f){b({usage:e,quota:f})},function(e){c(e)}):c(Error("webkitTemporaryStorage is not supported."))})}
D("ytglobal.storageClass_",Mw);function jn(a,b){var c=this;this.handleError=a;this.h=b;this.i=!1;void 0===self.document||self.addEventListener("beforeunload",function(){c.i=!0});
this.j=Math.random()<=T("ytidb_transaction_ended_event_rate_limit_session",.2)}
jn.prototype.Jb=function(a){this.handleError(a)};
jn.prototype.logEvent=function(a,b){switch(a){case "IDB_DATA_CORRUPTED":S("idb_data_corrupted_killswitch")||this.h("idbDataCorrupted",b);break;case "IDB_UNEXPECTEDLY_CLOSED":this.h("idbUnexpectedlyClosed",b);break;case "IS_SUPPORTED_COMPLETED":S("idb_is_supported_completed_killswitch")||this.h("idbIsSupportedCompleted",b);break;case "QUOTA_EXCEEDED":Pw(this,b);break;case "TRANSACTION_ENDED":this.j&&Math.random()<=T("ytidb_transaction_ended_event_rate_limit_transaction",.1)&&this.h("idbTransactionEnded",
b);break;case "TRANSACTION_UNEXPECTEDLY_ABORTED":a=Object.assign({},b,{hasWindowUnloaded:this.i}),this.h("idbTransactionAborted",a)}};
function Pw(a,b){Nw().estimate().then(function(c){c=Object.assign({},b,{isSw:void 0===self.document,isIframe:self!==self.top,deviceStorageUsageMbytes:Qw(null==c?void 0:c.usage),deviceStorageQuotaMbytes:Qw(null==c?void 0:c.quota)});a.h("idbQuotaExceeded",c)})}
function Qw(a){return"undefined"===typeof a?"-1":String(Math.ceil(a/1048576))}
;function Rw(){this.i=[];this.isReady=!1;this.j={};var a=this.h=new Nt(!!R("WIDGET_ID_ENFORCE")),b=this.He.bind(this);a.l=b;a.m=null;this.h.channel="widget";if(a=R("WIDGET_ID"))this.h.sessionId=a}
m=Rw.prototype;m.He=function(a,b,c){"addEventListener"===a&&b?this.Dc(b[0],c):this.Wc(a,b,c)};
m.Wc=function(){};
m.wc=function(a){var b=this;return function(c){return b.sendMessage(a,c)}};
m.Dc=function(a,b){this.j[a]||"onReady"===a||(this.addEventListener(a,this.wc(a,b)),this.j[a]=!0)};
m.addEventListener=function(){};
m.ee=function(){this.isReady=!0;this.sendMessage("initialDelivery",this.zc());this.sendMessage("onReady");gb(this.i,this.Bd,this);this.i=[]};
m.zc=function(){return null};
function Sw(a,b){a.sendMessage("infoDelivery",b)}
m.Bd=function(a){this.isReady?this.h.sendMessage(a):this.i.push(a)};
m.sendMessage=function(a,b){this.Bd({event:a,info:void 0===b?null:b})};
m.dispose=function(){this.h=null};var Tw={},Uw=(Tw["api.invalidparam"]=2,Tw.auth=150,Tw["drm.auth"]=150,Tw["heartbeat.net"]=150,Tw["heartbeat.servererror"]=150,Tw["heartbeat.stop"]=150,Tw["html5.unsupportedads"]=5,Tw["fmt.noneavailable"]=5,Tw["fmt.decode"]=5,Tw["fmt.unplayable"]=5,Tw["html5.missingapi"]=5,Tw["html5.unsupportedlive"]=5,Tw["drm.unavailable"]=5,Tw["mrm.blocked"]=151,Tw);var Vw=new Set("endSeconds startSeconds mediaContentUrl suggestedQuality videoId rct rctn".split(" "));function Ww(a){return(0===a.search("cue")||0===a.search("load"))&&"loadModule"!==a}
function Xw(a,b,c){if("string"===typeof a)return{videoId:a,startSeconds:b,suggestedQuality:c};b={};c=v(Vw);for(var d=c.next();!d.done;d=c.next())d=d.value,a[d]&&(b[d]=a[d]);return b}
function Yw(a,b,c,d){if(Ra(a)&&!Array.isArray(a)){b="playlist list listType index startSeconds suggestedQuality".split(" ");c={};for(d=0;d<b.length;d++){var e=b[d];a[e]&&(c[e]=a[e])}return c}b={index:b,startSeconds:c,suggestedQuality:d};"string"===typeof a&&16===a.length?b.list="PL"+a:b.playlist=a;return b}
;function Zw(a){Rw.call(this);this.listeners=[];this.l=!1;this.api=a;this.addEventListener("onReady",this.onReady.bind(this));this.addEventListener("onVideoProgress",this.Ue.bind(this));this.addEventListener("onVolumeChange",this.Ve.bind(this));this.addEventListener("onApiChange",this.Pe.bind(this));this.addEventListener("onPlaybackQualityChange",this.Re.bind(this));this.addEventListener("onPlaybackRateChange",this.Se.bind(this));this.addEventListener("onStateChange",this.Te.bind(this));this.addEventListener("onWebglSettingsChanged",
this.We.bind(this))}
w(Zw,Rw);m=Zw.prototype;
m.Wc=function(a,b,c){if(this.api.isExternalMethodAvailable(a,c)){b=b||[];if(0<b.length&&Ww(a)){var d=b;if(Ra(d[0])&&!Array.isArray(d[0]))var e=d[0];else switch(e={},a){case "loadVideoById":case "cueVideoById":e=Xw(d[0],void 0!==d[1]?Number(d[1]):void 0,d[2]);break;case "loadVideoByUrl":case "cueVideoByUrl":e=d[0];"string"===typeof e&&(e={mediaContentUrl:e,startSeconds:void 0!==d[1]?Number(d[1]):void 0,suggestedQuality:d[2]});b:{if((d=e.mediaContentUrl)&&(d=/\/([ve]|embed)\/([^#?]+)/.exec(d))&&d[2]){d=
d[2];break b}d=null}e.videoId=d;e=Xw(e);break;case "loadPlaylist":case "cuePlaylist":e=Yw(d[0],d[1],d[2],d[3])}b.length=1;b[0]=e}this.api.handleExternalCall(a,b,c);Ww(a)&&Sw(this,this.zc())}};
m.Dc=function(a,b){"onReady"===a?this.api.logApiCall(a+" invocation",b):"onError"===a&&this.l&&(this.api.logApiCall(a+" invocation",b,this.errorCode),this.errorCode=void 0);this.api.logApiCall(a+" registration",b);Rw.prototype.Dc.call(this,a,b)};
m.wc=function(a,b){var c=this,d=Rw.prototype.wc.call(this,a,b);return function(e){"onError"===a?c.api.logApiCall(a+" invocation",b,e):c.api.logApiCall(a+" invocation",b);d(e)}};
m.onReady=function(){var a=this.h,b=this.ee.bind(this);a.h=b;a=this.api.getVideoData();if(!a.isPlayable){this.l=!0;a=a.errorCode;var c=void 0===c?5:c;this.errorCode=a?Uw[a]||c:c;this.sendMessage("onError",this.errorCode.toString())}};
m.addEventListener=function(a,b){this.listeners.push({eventType:a,listener:b});this.api.addEventListener(a,b)};
m.zc=function(){if(!this.api)return null;var a=this.api.getApiInterface();lb(a,"getVideoData");for(var b={apiInterface:a},c=0,d=a.length;c<d;c++){var e=a[c];if(0===e.search("get")||0===e.search("is")){var f=0;0===e.search("get")?f=3:0===e.search("is")&&(f=2);f=e.charAt(f).toLowerCase()+e.substr(f+1);try{var g=this.api[e]();b[f]=g}catch(h){}}}b.videoData=this.api.getVideoData();b.currentTimeLastUpdated_=Date.now()/1E3;return b};
m.Te=function(a){a={playerState:a,currentTime:this.api.getCurrentTime(),duration:this.api.getDuration(),videoData:this.api.getVideoData(),videoStartBytes:0,videoBytesTotal:this.api.getVideoBytesTotal(),videoLoadedFraction:this.api.getVideoLoadedFraction(),playbackQuality:this.api.getPlaybackQuality(),availableQualityLevels:this.api.getAvailableQualityLevels(),currentTimeLastUpdated_:Date.now()/1E3,playbackRate:this.api.getPlaybackRate(),mediaReferenceTime:this.api.getMediaReferenceTime()};this.api.getVideoUrl&&
(a.videoUrl=this.api.getVideoUrl());this.api.getVideoContentRect&&(a.videoContentRect=this.api.getVideoContentRect());this.api.getProgressState&&(a.progressState=this.api.getProgressState());this.api.getPlaylist&&(a.playlist=this.api.getPlaylist());this.api.getPlaylistIndex&&(a.playlistIndex=this.api.getPlaylistIndex());this.api.getStoryboardFormat&&(a.storyboardFormat=this.api.getStoryboardFormat());Sw(this,a)};
m.Re=function(a){Sw(this,{playbackQuality:a})};
m.Se=function(a){Sw(this,{playbackRate:a})};
m.Pe=function(){for(var a=this.api.getOptions(),b={namespaces:a},c=0,d=a.length;c<d;c++){var e=a[c],f=this.api.getOptions(e);a.join(", ");b[e]={options:f};for(var g=0,h=f.length;g<h;g++){var k=f[g],l=this.api.getOption(e,k);b[e][k]=l}}this.sendMessage("apiInfoDelivery",b)};
m.Ve=function(){Sw(this,{muted:this.api.isMuted(),volume:this.api.getVolume()})};
m.Ue=function(a){a={currentTime:a,videoBytesLoaded:this.api.getVideoBytesLoaded(),videoLoadedFraction:this.api.getVideoLoadedFraction(),currentTimeLastUpdated_:Date.now()/1E3,playbackRate:this.api.getPlaybackRate(),mediaReferenceTime:this.api.getMediaReferenceTime()};this.api.getProgressState&&(a.progressState=this.api.getProgressState());Sw(this,a)};
m.We=function(){var a={sphericalProperties:this.api.getSphericalProperties()};Sw(this,a)};
m.dispose=function(){Rw.prototype.dispose.call(this);for(var a=0;a<this.listeners.length;a++){var b=this.listeners[a];this.api.removeEventListener(b.eventType,b.listener)}this.listeners=[]};function $w(a){H.call(this);this.h={};this.started=!1;this.connection=a;this.connection.subscribe("command",this.wd,this)}
w($w,H);m=$w.prototype;m.start=function(){this.started||this.Z()||(this.started=!0,this.connection.jb("RECEIVING"))};
m.jb=function(a,b){this.started&&!this.Z()&&this.connection.jb(a,b)};
m.wd=function(a,b,c){if(this.started&&!this.Z()){var d=b||{};switch(a){case "addEventListener":"string"===typeof d.event&&this.addListener(d.event);break;case "removeEventListener":"string"===typeof d.event&&this.removeListener(d.event);break;default:this.api.isReady()&&this.api.isExternalMethodAvailable(a,c||null)&&(b=ax(a,b||{}),c=this.api.handleExternalCall(a,b,c||null),(c=bx(a,c))&&this.jb(a,c))}}};
m.addListener=function(a){if(!(a in this.h)){var b=this.Qe.bind(this,a);this.h[a]=b;this.addEventListener(a,b)}};
m.Qe=function(a,b){this.started&&!this.Z()&&this.connection.jb(a,this.yc(a,b))};
m.yc=function(a,b){if(null!=b)return{value:b}};
m.removeListener=function(a){a in this.h&&(this.removeEventListener(a,this.h[a]),delete this.h[a])};
m.R=function(){this.connection.unsubscribe("command",this.wd,this);this.connection=null;for(var a in this.h)this.h.hasOwnProperty(a)&&this.removeListener(a);H.prototype.R.call(this)};function cx(a,b){$w.call(this,b);this.api=a;this.start()}
w(cx,$w);cx.prototype.addEventListener=function(a,b){this.api.addEventListener(a,b)};
cx.prototype.removeEventListener=function(a,b){this.api.removeEventListener(a,b)};
function ax(a,b){switch(a){case "loadVideoById":return a=Xw(b),[a];case "cueVideoById":return a=Xw(b),[a];case "loadVideoByPlayerVars":return[b];case "cueVideoByPlayerVars":return[b];case "loadPlaylist":return a=Yw(b),[a];case "cuePlaylist":return a=Yw(b),[a];case "seekTo":return[b.seconds,b.allowSeekAhead];case "playVideoAt":return[b.index];case "setVolume":return[b.volume];case "setPlaybackQuality":return[b.suggestedQuality];case "setPlaybackRate":return[b.suggestedRate];case "setLoop":return[b.loopPlaylists];
case "setShuffle":return[b.shufflePlaylist];case "getOptions":return[b.module];case "getOption":return[b.module,b.option];case "setOption":return[b.module,b.option,b.value];case "handleGlobalKeyDown":return[b.keyCode,b.shiftKey,b.ctrlKey,b.altKey,b.metaKey,b.key,b.code]}return[]}
function bx(a,b){switch(a){case "isMuted":return{muted:b};case "getVolume":return{volume:b};case "getPlaybackRate":return{playbackRate:b};case "getAvailablePlaybackRates":return{availablePlaybackRates:b};case "getVideoLoadedFraction":return{videoLoadedFraction:b};case "getPlayerState":return{playerState:b};case "getCurrentTime":return{currentTime:b};case "getPlaybackQuality":return{playbackQuality:b};case "getAvailableQualityLevels":return{availableQualityLevels:b};case "getDuration":return{duration:b};
case "getVideoUrl":return{videoUrl:b};case "getVideoEmbedCode":return{videoEmbedCode:b};case "getPlaylist":return{playlist:b};case "getPlaylistIndex":return{playlistIndex:b};case "getOptions":return{options:b};case "getOption":return{option:b}}}
cx.prototype.yc=function(a,b){switch(a){case "onReady":return;case "onStateChange":return{playerState:b};case "onPlaybackQualityChange":return{playbackQuality:b};case "onPlaybackRateChange":return{playbackRate:b};case "onError":return{errorCode:b}}return $w.prototype.yc.call(this,a,b)};
cx.prototype.R=function(){$w.prototype.R.call(this);delete this.api};function dx(a,b,c){pu.call(this);this.j=a;this.i=b;this.id=c}
w(dx,pu);dx.prototype.jb=function(a,b){this.Z()||this.j.jb(this.i,this.id,a,b)};
dx.prototype.R=function(){this.i=this.j=null;pu.prototype.R.call(this)};function ex(a,b,c){H.call(this);this.h=a;this.origin=c;this.i=br(window,"message",this.j.bind(this));this.connection=new dx(this,a,b);tc(this,this.connection)}
w(ex,H);ex.prototype.jb=function(a,b,c,d){this.Z()||a!==this.h||(a={id:b,command:c},d&&(a.data=d),this.h.postMessage(JSON.stringify(a),this.origin))};
ex.prototype.j=function(a){if(!this.Z()&&a.origin===this.origin){var b=a.data;if("string"===typeof b){try{b=JSON.parse(b)}catch(d){return}if(b.command){var c=this.connection;c.Z()||c.l("command",b.command,b.data,a.origin)}}}};
ex.prototype.R=function(){cr(this.i);this.h=null;H.prototype.R.call(this)};var fx=new Fw;function gx(){return fx.Tc()}
function hx(a){a=void 0===a?{}:a;return fx.invoke(a)}
;function ix(a,b,c,d,e){H.call(this);var f=this;this.A=b;this.webPlayerContextConfig=d;this.pc=e;this.Pa=!1;this.api={};this.ha=this.m=null;this.V=new L;this.h={};this.ba=this.ta=this.elementId=this.Za=this.config=null;this.Y=!1;this.j=this.D=null;this.Ba={};this.qc=["onReady"];this.lastError=null;this.Qb=NaN;this.S={};this.ea=0;this.i=this.l=a;tc(this,this.V);jx(this);c?this.ea=setTimeout(function(){f.loadNewVideoConfig(c)},0):d&&(kx(this),lx(this))}
w(ix,H);m=ix.prototype;m.getId=function(){return this.A};
m.loadNewVideoConfig=function(a){if(!this.Z()){this.ea&&(clearTimeout(this.ea),this.ea=0);var b=a||{};b instanceof Ot||(b=new Ot(b));this.config=b;this.setConfig(a);lx(this);this.isReady()&&mx(this)}};
function kx(a){var b;a.webPlayerContextConfig?b=a.webPlayerContextConfig.rootElementId:b=a.config.attrs.id;a.elementId=b||a.elementId;"video-player"===a.elementId&&(a.elementId=a.A,a.webPlayerContextConfig?a.webPlayerContextConfig.rootElementId=a.A:a.config.attrs.id=a.A);var c;(null==(c=a.i)?void 0:c.id)===a.elementId&&(a.elementId+="-player",a.webPlayerContextConfig?a.webPlayerContextConfig.rootElementId=a.elementId:a.config.attrs.id=a.elementId)}
m.setConfig=function(a){this.Za=a;this.config=nx(a);kx(this);if(!this.ta){var b;this.ta=ox(this,(null==(b=this.config.args)?void 0:b.jsapicallback)||"onYouTubePlayerReady")}this.config.args?this.config.args.jsapicallback=null:this.config.args={jsapicallback:null};var c;if(null==(c=this.config)?0:c.attrs)a=this.config.attrs,(b=a.width)&&this.i&&(this.i.style.width=pi(Number(b)||b)),(a=a.height)&&this.i&&(this.i.style.height=pi(Number(a)||a))};
function mx(a){if(a.config&&!0!==a.config.loaded)if(a.config.loaded=!0,!a.config.args||"0"!==a.config.args.autoplay&&0!==a.config.args.autoplay&&!1!==a.config.args.autoplay){var b;a.api.loadVideoByPlayerVars(null!=(b=a.config.args)?b:null)}else a.api.cueVideoByPlayerVars(a.config.args)}
function px(a){var b=!0,c=qx(a);c&&a.config&&(b=c.dataset.version===rx(a));return b&&!!E("yt.player.Application.create")}
function lx(a){if(!a.Z()&&!a.Y){var b=px(a);if(b&&"html5"===(qx(a)?"html5":null))a.ba="html5",a.isReady()||sx(a);else if(tx(a),a.ba="html5",b&&a.j&&a.l)a.l.appendChild(a.j),sx(a);else{a.config&&(a.config.loaded=!0);var c=!1;a.D=function(){c=!0;var d=ux(a,"player_bootstrap_method")?E("yt.player.Application.createAlternate")||E("yt.player.Application.create"):E("yt.player.Application.create");var e=a.config?nx(a.config):void 0;d&&d(a.l,e,a.webPlayerContextConfig,a.pc);sx(a)};
a.Y=!0;b?a.D():(Zt(rx(a),a.D),(b=vx(a))&&gu(b),wx(a)&&!c&&D("yt.player.Application.create",null))}}}
function qx(a){var b=vd(a.elementId);!b&&a.i&&a.i.querySelector&&(b=a.i.querySelector("#"+a.elementId));return b}
function sx(a){if(!a.Z()){var b=qx(a),c=!1;b&&b.getApiInterface&&b.getApiInterface()&&(c=!0);if(c){a.Y=!1;if(!ux(a,"html5_remove_not_servable_check_killswitch")){var d;if((null==b?0:b.isNotServable)&&a.config&&(null==b?0:b.isNotServable(null==(d=a.config.args)?void 0:d.video_id)))return}xx(a)}else a.Qb=setTimeout(function(){sx(a)},50)}}
function xx(a){jx(a);a.Pa=!0;var b=qx(a);if(b){a.m=yx(a,b,"addEventListener");a.ha=yx(a,b,"removeEventListener");var c=b.getApiInterface();c=c.concat(b.getInternalApiInterface());for(var d=a.api,e=0;e<c.length;e++){var f=c[e];d[f]||(d[f]=yx(a,b,f))}}for(var g in a.h)a.h.hasOwnProperty(g)&&a.m&&a.m(g,a.h[g]);mx(a);a.ta&&a.ta(a.api);a.V.Ya("onReady",a.api)}
function yx(a,b,c){var d=b[c];return function(){var e=B.apply(0,arguments);try{return a.lastError=null,d.apply(b,e)}catch(f){if("sendAbandonmentPing"!==c)throw f.params=c,a.lastError=f,e=new V("PlayerProxy error in method call",{error:f,method:c,playerId:a.A}),e.level="WARNING",e;}}}
function jx(a){a.Pa=!1;if(a.ha)for(var b in a.h)a.h.hasOwnProperty(b)&&a.ha(b,a.h[b]);for(var c in a.S)a.S.hasOwnProperty(c)&&clearTimeout(Number(c));a.S={};a.m=null;a.ha=null;b=a.api;for(var d in b)b.hasOwnProperty(d)&&(b[d]=null);b.addEventListener=function(e,f){a.addEventListener(e,f)};
b.removeEventListener=function(e,f){a.removeEventListener(e,f)};
b.destroy=function(){a.dispose()};
b.getLastError=function(){return a.getLastError()};
b.getPlayerType=function(){return a.getPlayerType()};
b.getCurrentVideoConfig=function(){return a.Za};
b.loadNewVideoConfig=function(e){a.loadNewVideoConfig(e)};
b.isReady=function(){return a.isReady()}}
m.isReady=function(){return this.Pa};
m.addEventListener=function(a,b){var c=this,d=ox(this,b);d&&(0<=fb(this.qc,a)||this.h[a]||(b=zx(this,a),this.m&&this.m(a,b)),this.V.subscribe(a,d),"onReady"===a&&this.isReady()&&setTimeout(function(){d(c.api)},0))};
m.removeEventListener=function(a,b){this.Z()||(b=ox(this,b))&&this.V.unsubscribe(a,b)};
function ox(a,b){var c=b;if("string"===typeof b){if(a.Ba[b])return a.Ba[b];c=function(){var d=B.apply(0,arguments),e=E(b);if(e)try{e.apply(C,d)}catch(f){throw d=new V("PlayerProxy error when executing callback",{error:f}),d.level="ERROR",d;}};
a.Ba[b]=c}return c?c:null}
function zx(a,b){function c(d){var e=setTimeout(function(){if(!a.Z()){try{a.V.Ya(b,null!=d?d:void 0)}catch(h){var f=new V("PlayerProxy error when creating global callback",{error:h.message,event:b,playerId:a.A,data:d,originalStack:h.stack});f.level="WARNING";throw f;}f=a.S;var g=String(e);g in f&&delete f[g]}},0);
rb(a.S,String(e))}
return a.h[b]=c}
m.getPlayerType=function(){return this.ba||(qx(this)?"html5":null)};
m.getLastError=function(){return this.lastError};
function tx(a){a.cancel();jx(a);a.ba=null;a.config&&(a.config.loaded=!1);var b=qx(a);b&&(px(a)||!wx(a)?a.j=b:(b&&b.destroy&&b.destroy(),a.j=null));if(a.l)for(a=a.l;b=a.firstChild;)a.removeChild(b)}
m.cancel=function(){this.D&&eu(rx(this),this.D);clearTimeout(this.Qb);this.Y=!1};
m.R=function(){tx(this);if(this.j&&this.config&&this.j.destroy)try{this.j.destroy()}catch(b){var a=new V("PlayerProxy error during disposal",{error:b});a.level="ERROR";throw a;}this.Ba=null;for(a in this.h)this.h.hasOwnProperty(a)&&delete this.h[a];this.Za=this.config=this.api=null;delete this.l;delete this.i;H.prototype.R.call(this)};
function wx(a){var b,c;a=null==(b=a.config)?void 0:null==(c=b.args)?void 0:c.fflags;return!!a&&-1!==a.indexOf("player_destroy_old_version=true")}
function rx(a){return a.webPlayerContextConfig?a.webPlayerContextConfig.jsUrl:(a=a.config.assets)?a.js:""}
function vx(a){return a.webPlayerContextConfig?a.webPlayerContextConfig.cssUrl:(a=a.config.assets)?a.css:""}
function ux(a,b){if(a.webPlayerContextConfig)var c=a.webPlayerContextConfig.serializedExperimentFlags;else{var d;if(null==(d=a.config)?0:d.args)c=a.config.args.fflags}return(c||"").split("&").includes(b+"=true")}
function nx(a){for(var b={},c=v(Object.keys(a)),d=c.next();!d.done;d=c.next()){d=d.value;var e=a[d];b[d]="object"===typeof e?ub(e):e}return b}
;var Ax={},Bx="player_uid_"+(1E9*Math.random()>>>0);function Cx(a,b){var c="player",d=!1;d=void 0===d?!0:d;c="string"===typeof c?vd(c):c;var e=Bx+"_"+Sa(c),f=Ax[e];if(f&&d)return Dx(a,b)?f.api.loadVideoByPlayerVars(a.args||null):f.loadNewVideoConfig(a),f.api;f=new ix(c,e,a,b,void 0);Ax[e]=f;f.addOnDisposeCallback(function(){delete Ax[f.getId()]});
return f.api}
function Dx(a,b){return b&&b.serializedExperimentFlags?b.serializedExperimentFlags.includes("web_player_remove_playerproxy=true"):a&&a.args&&a.args.fflags?a.args.fflags.includes("web_player_remove_playerproxy=true"):!1}
;var Ex=null,Fx=null,Gx=null;
function Hx(){Sv();var a=hm(),b=km(119),c=1<window.devicePixelRatio;if(document.body&&Fi(document.body,"exp-invert-logo"))if(c&&!Fi(document.body,"inverted-hdpi")){var d=document.body;if(d.classList)d.classList.add("inverted-hdpi");else if(!Fi(d,"inverted-hdpi")){var e=Di(d);Ei(d,e+(0<e.length?" inverted-hdpi":"inverted-hdpi"))}}else!c&&Fi(document.body,"inverted-hdpi")&&Gi();if(b!=c){b="f"+(Math.floor(119/31)+1);d=lm(b)||0;d=c?d|67108864:d&-67108865;0===d?delete em[b]:(c=d.toString(16),em[b]=c.toString());
c=!0;S("web_secure_pref_cookie_killswitch")&&(c=!1);b=a.h;d=[];for(f in em)em.hasOwnProperty(f)&&d.push(f+"="+encodeURIComponent(String(em[f])));var f=d.join("&");am(b,f,63072E3,a.i,c)}}
function Ix(){Jx()}
function Kx(){Rv("ep_init_pr");Jx()}
function Jx(){var a=Ex.getVideoData(1);a=a.title?a.title+" - YouTube":"YouTube";document.title!==a&&(document.title=a)}
function Lx(){Ex&&Ex.sendAbandonmentPing&&Ex.sendAbandonmentPing();R("PL_ATT")&&fx.dispose();for(var a=vi,b=0,c=Aw.length;b<c;b++)a.qa(Aw[b]);Aw.length=0;du("//static.doubleclick.net/instream/ad_status.js");Bw=!1;Uk("DCLKSTAT",0);sc(Gx,Fx);Ex&&(Ex.removeEventListener("onVideoDataChange",Ix),Ex.destroy())}
;D("yt.setConfig",Uk);D("yt.config.set",Uk);D("yt.setMsg",Wt);D("yt.msgs.set",Wt);D("yt.logging.errors.log",Us);
D("writeEmbed",function(){var a=R("PLAYER_CONFIG");if(!a){var b=R("PLAYER_VARS");b&&(a={args:b})}Mu(!0);"gvn"===a.args.ps&&(document.body.style.backgroundColor="transparent");a.attrs||(a.attrs={width:"100%",height:"100%",id:"video-player"});var c=document.referrer;b=R("POST_MESSAGE_ORIGIN");window!==window.top&&c&&c!==document.URL&&(a.args.loaderUrl=c);Ov("embed",["ol"]);c=R("WEB_PLAYER_CONTEXT_CONFIGS").WEB_PLAYER_CONTEXT_CONFIG_ID_EMBEDDED_PLAYER;if(!c.serializedForcedExperimentIds){var d=hl(window.location.href);
d.forced_experiments&&(c.serializedForcedExperimentIds=d.forced_experiments)}var e;(null==(e=a.args)?0:e.autoplay)&&Ov("watch",["pbs","pbu","pbp"]);Ex=Cx(a,c);Ex.addEventListener("onVideoDataChange",Ix);Ex.addEventListener("onReady",Kx);a=R("POST_MESSAGE_ID","player");R("ENABLE_JS_API")?Gx=new Zw(Ex):R("ENABLE_POST_API")&&"string"===typeof a&&"string"===typeof b&&(Fx=new ex(window.parent,a,b),Gx=new cx(Ex,Fx.connection));Cw();S("ytidb_create_logger_embed_killswitch")||hn();a={};Lw.h||(Lw.h=new Lw);
Lw.h.install((a.flush_logs={callback:function(){As()}},a));
Sq();S("ytidb_clear_embedded_player")&&vi.pa(function(){var f,g;if(!nw){var h=Er();Ar(h,{kc:mw,Id:kw});var k={cd:{feedbackEndpoint:Yu(ew),modifyChannelNotificationPreferenceEndpoint:Yu(fw),playlistEditEndpoint:Yu(gw),subscribeEndpoint:Yu(cw),unsubscribeEndpoint:Yu(dw),webPlayerShareEntityServiceEndpoint:Yu(hw)}},l=Vu(),n={};l&&(n.client_location=l);void 0===f&&(f=Wl());void 0===g&&(g=h.resolve(mw));Xv(k,g,f,n);Ar(h,{kc:bw,Jd:Wv.h});nw=h.resolve(bw)}ww()})});
D("yt.abuse.player.botguardInitialized",E("yt.abuse.player.botguardInitialized")||gx);D("yt.abuse.player.invokeBotguard",E("yt.abuse.player.invokeBotguard")||hx);D("yt.abuse.dclkstatus.checkDclkStatus",E("yt.abuse.dclkstatus.checkDclkStatus")||Dw);D("yt.player.exports.navigate",E("yt.player.exports.navigate")||Lu);D("yt.util.activity.init",E("yt.util.activity.init")||fr);D("yt.util.activity.getTimeSinceActive",E("yt.util.activity.getTimeSinceActive")||ir);
D("yt.util.activity.setTimestamp",E("yt.util.activity.setTimestamp")||gr);window.addEventListener("load",Yk(function(){Hx()}));
window.addEventListener("pageshow",Yk(function(a){a.persisted||Hx()}));
window.addEventListener("pagehide",Yk(function(a){S("embeds_web_enable_dispose_player_if_page_not_cached_killswitch")?Lx():a.persisted||Lx()}));
window.onerror=function(a,b,c,d,e){b=void 0===b?"Unknown file":b;c=void 0===c?0:c;var f=!1,g=Vk("log_window_onerror_fraction");if(g&&Math.random()<g)f=!0;else{g=document.getElementsByTagName("script");for(var h=0,k=g.length;h<k;h++)if(0<g[h].src.indexOf("/debug-")){f=!0;break}}f&&(f=!1,e?f=!0:("string"===typeof a?g=a:ErrorEvent&&a instanceof ErrorEvent?(f=!0,g=a.message,b=a.filename,c=a.lineno,d=a.colno):(g="Unknown error",b="Unknown file",c=0),e=new V(g),e.name="UnhandledWindowError",e.message=g,
e.fileName=b,e.lineNumber=c,isNaN(d)?delete e.columnNumber:e.columnNumber=d),f?Us(e):Vs(e))};
$d=Ws;window.addEventListener("unhandledrejection",function(a){Ws(a.reason)});
gb(R("ERRORS")||[],function(a){Us.apply(null,a)});
Uk("ERRORS",[]);S("embeds_web_enable_scheduler_to_player_binary")&&Zm();}).call(this);
