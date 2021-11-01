import React from 'react';
import axios from 'axios';
import {Table} from 'antd';
class Targets extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            targets: [],
            loading: true
        }
    }

    async getTargetsData() {
        try {
            const res = await axios.get('http://localhost:8080/api/v1/target')
            this.setState({ loading: false, targets: res.data })
        } catch {
            console.error("Could not get targets")
        }
    }

    componentDidMount() {
        this.getTargetsData()
    }

    render() {
        const columns = [
            {
                title: 'ID',
                key: 'id',
                dataIndex: 'id'
            },
            {
                title: 'Name',
                key: 'name',
                dataIndex: 'name'
            },
            {
                title: 'Schema',
                key: 'conf_blob',
                dataIndex: 'conf_blob',
                render: d => JSON.stringify(d)
            }
        ]
        return (<div style={{ height: 400, width: '70%' }}>
                <Table
                    dataSource = {this.state.targets}
                    columns = {columns}
                />
                </div>
        );
    }
}

export default Targets;