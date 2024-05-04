import { app } from "/scripts/app.js";
import { ComfyWidgets } from "/scripts/widgets.js";

app.registerExtension({
    name: "Comfy.D2.D2_RefinerStepsTester",
    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        if (nodeData.name !== "D2 Refiner Steps Tester") return;

        // 以下、カスタムノード処理
        function populate(text) {
            // すでに表示しているものがあれば削除
            // 1番目はseedなので残す
            if (this.widgets) {
                for (let i = 1; i < this.widgets.length; i++) {
                    this.widgets[i].onRemove?.();
                }
                this.widgets.length = 1;
            }

            // 文字列はなぜか配列で送られてくるので結合
            const showText = text.join("");
            const widget = ComfyWidgets["STRING"](
                this,
                "text",
                ["STRING", { multiline: true }],
                app
            ).widget;
            widget.inputEl.readOnly = true;
            widget.inputEl.style.opacity = 0.6;
            widget.value = showText;

            // requestAnimationFrame(() => {
            //     const sz = this.computeSize();
            //     if (sz[0] < this.size[0]) {
            //         sz[0] = this.size[0];
            //     }
            //     if (sz[1] < this.size[1]) {
            //         sz[1] = this.size[1];
            //     }
            //     this.onResize?.(sz);
            //     app.graph.setDirtyCanvas(true, false);
            // });
        }

        /**
         * ノード実行時
         */
        const onExecuted = nodeType.prototype.onExecuted;
        nodeType.prototype.onExecuted = function (message) {
            onExecuted?.apply(this, arguments);
            populate.call(this, message.text);
        };

        const onConfigure = nodeType.prototype.onConfigure;
        nodeType.prototype.onConfigure = function () {
            onConfigure?.apply(this, arguments);
            // if (this.widgets_values?.length) {
            //     populate.call(this, this.widgets_values);
            // }
        };

        /**
         * ノード作成時
         * ノードのWdget（入力欄など）を精査し、seedだったら非表示にする
         */
        const orgOnNodeCreated = nodeType.prototype.onNodeCreated;
        nodeType.prototype.onNodeCreated = function () {
            const result = orgOnNodeCreated
                ? orgOnNodeCreated.apply(this)
                : undefined;

            for (const widget of this.widgets) {
                if (widget.name === "seed") {
                    widget.type = "converted-widget";
                    if (!widget.linkedWidgets) continue;
                    for (const lw of widget.linkedWidgets) {
                        lw.type = "converted-widget";
                    }
                }
            }
            return result;
        };
    },
});
