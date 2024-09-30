var h=Object.defineProperty;var d=(a,e,t)=>e in a?h(a,e,{enumerable:!0,configurable:!0,writable:!0,value:t}):a[e]=t;var s=(a,e,t)=>d(a,typeof e!="symbol"?e+"":e,t);class p{constructor({id:e,label:t,className:n="myButton",url:r="#"}){s(this,"id");s(this,"label");s(this,"className");s(this,"url");s(this,"clickCallback");this.id=e,this.label=t,this.className=n,this.url=r}onClick(e){this.clickCallback=e}getElement(e){const t=document.createElement("template");t.innerHTML=e;const n=t.content.firstChild;return this.clickCallback!=null&&n.addEventListener("click",()=>{this.clickCallback()}),n}toRequest(){return{id:this.id,label:this.label,css_class:this.className,url:this.url}}getEndPoint(){return"createButton"}}var i=(a=>(a.Text="text",a.Number="number",a.Float="float",a))(i||{});class c{constructor({id:e,label:t,placeholder:n,type:r,className:o}){s(this,"id");s(this,"label");s(this,"className");s(this,"placeholder");s(this,"type");s(this,"changeCallback");this.id=e,this.label=t,this.className=o,this.placeholder=n,this.type=r}getElement(e){const t=document.createElement("template");t.innerHTML=e;const n=t.content.firstChild;return this.changeCallback==null||n.addEventListener("change",r=>{const o=r.target;this.changeCallback(this.parse(o.value))}),n}parse(e){if(this.type=="text")return e;let t=NaN;switch(this.type){case"number":t=parseInt(e);break;case"float":t=parseFloat(e);break}if(isNaN(t))throw new Error(`Cant cast value as ${this.type}, '${e}'`);return t}onChange(e){this.changeCallback=e}getEndPoint(){return"createInput"}toRequest(){return{id:this.id,label:this.label,css_class:this.className,placeholder:this.placeholder,type:this.type}}}async function l(a){const e=await m(a.getEndPoint(),a.toRequest());return a.getElement(e)}const u="/api/v1/components";async function m(a,e){try{const t=await fetch(`${u}/${a}`,{method:"POST",headers:[["Content-Type","application/json"]],body:JSON.stringify(e)});if(!t.ok){const r=await t.json();throw new Error(`HTTP error! Status: ${t.status} ${JSON.stringify(r)}`)}return(await t.json()).html}catch(t){console.error("There was a problem with the fetch operation:",t)}}function g(a,e){const t=document.getElementById(a);if(t==null)throw Error(`Failed to find drawer container with id ${a}`);const n=t.querySelector("div.drawer");if(n==null)throw Error(`Failed to find drawer within drawer container ${a}`);b(t),e.forEach(r=>{const o=document.createElement("div");o.className="component",o.appendChild(r),n.appendChild(o)})}function b(a){const e=a.querySelector("input");if(e==null)throw Error("Failed to find toggle");e.addEventListener("change",function(){const t=a.getElementsByClassName("drawer");for(let n=0;n<t.length;n++){const r=t[n];this.checked?r.classList.add("open"):r.classList.remove("open")}})}class C{constructor(e,t,n){s(this,"mapName");s(this,"maxSlope");s(this,"reduceBy");this.mapName=e,this.maxSlope=t,this.reduceBy=n}async setup(){const e=await Promise.all([this.createMapName(),this.createMaxSlope(),this.createReduceBy(),this.createButton()]);g("debugDrawer",e)}loadMap(){console.info(`Load Map: ${this.mapName}`),console.info(`Reduce By: ${this.reduceBy}`),console.info(`Max Slope: ${this.maxSlope}`)}createMaxSlope(){const e=new c({id:"maxSlopeInput",className:"label-input",label:"Max Slope",placeholder:`${this.maxSlope}`,type:i.Number});return e.onChange(t=>{this.maxSlopeChanged(t)}),l(e)}createButton(){const e=new p({id:"loadDebugMap",className:"myButton",label:"Load Map",url:"#"});return e.onClick(()=>{this.loadMap()}),l(e)}createReduceBy(){const e=new c({id:"reduceByInput",label:"Reduce By",placeholder:`${this.reduceBy}`,className:"label-input",type:i.Float});return e.onChange(t=>{this.reduceByChanged(t)}),l(e)}createMapName(){const e=new c({id:"loadDebugMap",className:"label-input",label:"Map",placeholder:`${this.mapName}`,type:i.Text});return e.onChange(t=>{this.mapNameChanged(t)}),l(e)}reduceByChanged(e){this.reduceBy=e}maxSlopeChanged(e){this.maxSlope=e}mapNameChanged(e){this.mapName=e}}const f=new C("adt_32_48",10,.5);f.setup();
